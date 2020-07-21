from flask_socketio import Namespace
from apps import socketio
from apps.utils.command import ps_command, top_command, tail_command


name_space = '/test'


# class MyCustomNameSpace(Namespace):
#
#     def on_connect(self):
#         print('连接')
#
#     def on_disconnect(self):
#         print("关闭连接")
#
#     def on_message(self, message):
#         print('recevice message', message)


# socketio.on_namespace(MyCustomNameSpace(name_space))

@socketio.on('connect', namespace="/shell")
def connect():
    print("connect..")


@socketio.on('disconnect', namespace="/shell")
def disconnect():
    print("disconnect..")


@socketio.on('client', namespace="/shell")
def client_info(data):
    print('client data', data)
    _type = data.get('_type')
    if _type == 'tail':
        tail_command.background_thread()
    elif _type == 'ps':
        ps_command.background_thread()
    elif _type == 'top':
        top_command.background_thread()
    else:
        socketio.emit('response', {'text': '未知命令'}, namespace='/shell')


@socketio.on('leave', namespace="/shell")
def leave(data):
    print('leave data', data)
    _type = data.get('_type')
    if _type == 'tail':
        tail_command.leave()
    elif _type == 'ps':
        ps_command.leave()
    elif _type == 'top':
        top_command.leave()
    else:
        socketio.emit('response', {'text': '未知命令'}, namespace='/shell')
