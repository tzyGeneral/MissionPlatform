from flask import render_template, redirect, url_for, session
from apps.admin import admin
from apps.admin.forms import AdminForm
from apps.admin.minddleware.middleware import admin_login_required

from apps import socketio
from apps.utils.command import ps_command, top_command, tail_command


@admin.route('/login', methods=['POST', 'GET'])
def login():
    form = AdminForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username and password:
            session['user_name'] = username
            return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/index')
@admin_login_required
def index():
    return render_template('admin/index.html')

@admin.route('/test')
def hello():
    return render_template('admin/test.html')


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

from apps.utils.TailLogFile import tail_command2
@socketio.on('log', namespace='/shell')
def log_info(data):
    _type = data.get('_type')
    if _type == 'tail':
        tail_command2.background_thread()

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
