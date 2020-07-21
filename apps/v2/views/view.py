from flask_restful import Resource
from flask import request


class HelloWordView(Resource):
    # 测试视图
    def get(self):
        message = request.args.get('message', '')
        data = 'hello word2' + message
        rsp = {'status': 200, 'msg': 'ok', 'data': data}
        return rsp
