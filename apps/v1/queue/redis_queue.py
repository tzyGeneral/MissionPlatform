import redis


pool = redis.ConnectionPool(host='127.0.0.1')


class RedisQueue:
    def __init__(self, name, namespace='queue'):
        self.__db = redis.Redis(connection_pool=pool)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        """
        返回队列里面list元素的数量
        :return:
        """
        return self.__db.llen(self.key)

    def put(self, item):
        """
        添加新元素到队列的最右方
        :param item:
        :return:
        """
        self.__db.rpush(self.key, item)

    def get_wait(self, timeout=30):
        """
        返回队列第一个元素,如果为空则等待至有元素被假如到队列
        :param timeout: 等待超时时间
        :return:
        """
        item = self.__db.blpop(self.key, timeout=timeout)
        return item

    def get_nowait(self):
        """
        直接返回队列里的第一个元素,如果队列为空返回的None
        :return:
        """
        item = self.__db.lpop(self.key)
        return item

    def putList(self, l):
        """
        添加列表到队列的最右方
        :param l:
        :return:
        """
        for item in l:
            self.__db.rpush(self.key, item)

    def getList(self, start, end):
        """
        一次性从队列中获取多个
        :param start:
        :param end:
        :return:
        """
        size = self.qsize()
        if size - 1 < end:
            end = size - 1
        elif start > end or start < 0:
            return []
        try:
            data = self.__db.lrange(self.key, start=start, end=end)
            self.__db.ltrim(self.key, start=0, end=start - 1)
            self.__db.ltrim(self.key, start=end + 1, end=-1)
        except Exception as e:
            print(e)
            return []
        return data
