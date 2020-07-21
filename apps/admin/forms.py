# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):
    username = StringField(
        validators=[
            DataRequired('请输入账号')
        ],
        id="userName",
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名"
        }
    )

    password = PasswordField(
        validators=[
            DataRequired('请输入密码')

        ],
        id="userPwd",
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码"
        }
    )

    submit = SubmitField(
        '登录',
        id='signinSubmit',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block"
        }
    )
