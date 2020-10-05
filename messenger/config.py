import os
from messenger.security import gen_rand_string

class Config:
    SECRET_KEY = gen_rand_string()
    SQLALCHEMY_DATABASE_URI = os.environ.get('STI_MSN_DB') or 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
