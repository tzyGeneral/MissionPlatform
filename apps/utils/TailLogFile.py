# coding=utf-8
import os
import re
import platform
import random
from threading import Lock
from config import LOG_FILE, EVENT_NAME, NAMESPACE
from apps.utils.cleanTailLog import regexLogLine

from apps import socketio


class Command:

    def __init__(self, cmd_name, event_name=None, name_space=None, *args, **kwargs):
        '''
        :param cmd_name: 命令名称
        :param event_name: socketio 事件名称
        :param name_space: socketio 名称空间
        '''
        self.lock = self.get_lock()
        self.close_thread = False
        self.thread = None
        self.client_num = 0  # 连入数量
        self.event_name = event_name
        self.namespace = name_space
        self.cmd_name = cmd_name

    def get_lock(self):
        return Lock()

    def stop(self):
        with self.lock:
            self.close_thread = True

    def incr(self, num=1):
        with self.lock:
            self.client_num += num
            if self.client_num < 0:
                self.client_num = 0
                self.close_thread = True

    def send_response(self, text, name):
        socketio.emit(self.event_name, {'text': text, 'name': name, '_type': self.cmd_name}, namespace=self.namespace)

    def sleep(self, seconds):
        socketio.sleep(seconds)

    def leave(self):
        self.incr(num=-1)
        print(f'离开{self.cmd_name},客户端还剩', self.client_num)


class TailCommand(Command):

    def background_thread(self):
        self.incr()
        print('有客户端进入tail页面，当前页面客户端数量为', self.client_num)
        with self.lock:
            if self.thread is None:
                self.close_thread = False
                self.thread = socketio.start_background_task(target=self.tail_f)

    def tail_f(self, log_path=LOG_FILE):

        try:
            tail_pipe = os.popen('tail -f ' + log_path)
        except:
            print('文件不存在')
            return
        else:
            while not self.close_thread:
                tail_output = tail_pipe.readline()
                if tail_output.strip():
                    rankDicList, nameList = regexLogLine(str(tail_output))
                    self.send_response(rankDicList, nameList)
                    self.sleep(1)
            tail_pipe.close()
            print('离开tail,客户端还剩', self.client_num)

        # while not self.close_thread:
        #     aodcode = ''.join([str(random.randint(1,5)) for _ in range(1)])
        #     rankDicList, nameList = regexLogLine(str(f'https://www.baidu.com?adcode={aodcode}'))
        #     self.send_response(rankDicList, nameList)
        #     self.sleep(1)
        #
        # print('离开tail,客户端还剩', self.client_num)


tail_command2 = TailCommand(cmd_name='tail', event_name=EVENT_NAME, name_space=NAMESPACE)
