# _*_ coding: utf-8 _*_

from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from wechat_sdk import WechatBasic as Basic, WechatConf as Conf


class Config:
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '$%^NB4%^#_+UHha'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


wechat_config = {'token': 'tetetetest',
                 'appid': 'wx1766a3244906ed6e',
                 'appsecret': '92c5bd5f5c759f53e0798c9bfc140c73',
                 'encrypt_mode': 'normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
                 # 如果传入 encoding_aes_key 值则必须保证同时传入 token, appid
                 'encoding_aes_key': 'uf2xUCwvr3lIsi2VPok9GO6cd9jb1lwwP2XSpW4vtPZ'
                 }

#实例化 Flask, SQLAlchemy, Wechat-SDK 基础对象并传入配置
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
conf = Conf(wechat_config)
wechat = Basic(conf=conf)

