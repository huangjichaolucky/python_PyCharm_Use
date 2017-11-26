# coding=utf-8
from flask import g
def login_log(username):
    print username
    print 'g.username %s' %g.username