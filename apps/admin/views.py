from flask import render_template, redirect, url_for, session
from apps.admin import admin
from apps.admin.forms import AdminForm
from apps.admin.minddleware.middleware import admin_login_required


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
