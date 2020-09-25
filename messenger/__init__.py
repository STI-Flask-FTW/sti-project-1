# -*- coding: utf-8 -*-

from .config import Config

from flask import Flask

APP = Flask(__name__)
APP.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
DB = SQLAlchemy(APP)

from messenger import views
