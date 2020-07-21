# encoding: utf-8
from flask import Flask
from config import Conf
from flask_cache import Cache
from flask_login import LoginManager
from flask_socketio import SocketIO


cache = Cache(config={'CACHE_TYPE': 'simple'}, with_jinja2_ext=False)
login_manager = LoginManager()
socketio = SocketIO()


def init_app(app):
    # 插件初始化
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return None


def register_blueprints(app):
    # 注册版本
    from apps.v1 import create_blueprint_v1
    from apps.v2 import create_blueprint_v2
    from apps.admin import admin as admin_blueprint

    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')
    app.register_blueprint(create_blueprint_v2(), url_prefix='/api/v2')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')


def create_app():
    # 创建app实例
    app = Flask(__name__)
    app.config.from_object(Conf)
    app.secret_key = app.config['SECRET_KEY']

    cache.init_app(app)
    init_app(app)
    register_blueprints(app)
    socketio.init_app(app)
    return app


app = create_app()
