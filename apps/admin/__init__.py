# -*- coding: utf-8 -*-
from flask import Blueprint


admin = Blueprint('admin', __name__)

from apps.admin import views