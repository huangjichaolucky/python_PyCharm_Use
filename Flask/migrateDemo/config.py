#-*- coding=utf-8 -*-

DEBUG = True
# url 格式
#dialect+driver://username:password@host:port/database
# mysql://root:root:@127.0.0.1:3306/datademo
#dialect 数据库的实现，比如MYSQL、SQLite 并且转成小写
# +driver 对应的驱动，若不指定，使用默认的驱动， 比如MYSQL 的是比如MYSQLdb
# username
# :password
# @host:
# port/ 端口号
# database 数据库名字
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'migratedemo'

#  疑问   此处 {}什么意思
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

