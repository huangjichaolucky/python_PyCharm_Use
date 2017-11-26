# -*- coding:utf-8 -*-
import os

DEBUG = True

#1疑问SECRET_KEY 作用是什么
SECRET_KEY = os.urandom(24)

HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'zlktqaDemo'
USERNAME = 'root'
PASSWORD = 'root'

# 2该字符串代表什么意思，  .format用处是什么
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=urf8'.format(USERNAME,
                                                              PASSWORD,
                                                              HOSTNAME,
                                                              PORT,
                                                              DATABASE)
SQLACHEMY_DATABASE_URL = DB_URL

