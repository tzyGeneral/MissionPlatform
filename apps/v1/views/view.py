from flask_restful import Resource
from flask import request


class HelloWordView(Resource):
    # 测试视图
    def get(self):
        message = request.args.get('message', '')
        data = 'hello word' + message
        rsp = {'status': 200, 'msg': 'ok', 'data': data}
        return rsp


class MissionView(Resource):
    # 爬虫任务下发平台
    def get(self):
        rsp = {'status': 200, 'msg': 'ok'}
        return rsp

    def post(self):
        rsp = {'status': 200, 'msg': 'ok'}
        try:
            key = request.form.get('key', '')
            item = request.form.get('item', '')
            if key == 'key':
                pass
        except Exception as e:
            rsp['status'] = 500
            rsp['msg'] = str(e)
        return rsp


class VisualizationView(Resource):
    # 爬虫任务可视化
    def get(self):
        rsp = {'status': 200, 'msg': 'ok'}
        return rsp
