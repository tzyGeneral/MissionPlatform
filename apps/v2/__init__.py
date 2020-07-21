# encoding: utf-8
from flask import Blueprint
from flask_restful import Api
from .views import view


def register_views(app):
    """路由注册"""
    api = Api(app)

    api.add_resource(view.HelloWordView, '/hello')


def create_blueprint_v2():
    """注册蓝图->v1版本"""
    bp_v1 = Blueprint('v2', __name__)
    register_views(bp_v1)
    return bp_v1
