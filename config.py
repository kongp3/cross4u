# -*- coding: utf-8 -*-
from flask import Flask

# 应用服务器配置
app = Flask(__name__, template_folder='./templates', static_folder='./static')
# app = Flask(__name__)
app_host = '0.0.0.0'
app_port = 31080

DL_ROOT = './static/download/'
WEB_HOST = "http://0.0.0.0:31080/"
