# -*- coding: utf-8 -*-
from functools import wraps
from flask import redirect, session, url_for


def admin_login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_name'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))

    return wrapper
