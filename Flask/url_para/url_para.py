#-*- coding=utf-8 -*-
from flask import Flask, url_for, redirect


app = Flask(__name__)


@app.route('/')
def hello_world():
    #可以将 视图函数转成 url地址
    print url_for('login')
    print url_for('articleID', id = '123455')
    return 'Hello World!'

#<> 中的 字符是 参数名
# 可访问 http://127.0.0.1:5000/article/xx
@app.route('/article/<id>/')
def articleID(id):
    return u'当前ID是 %s' % id

@app.route('/login/')
def login():
    return 'login 这是登陆页'

@app.route('/question/<is_Login>')
def question(is_Login):
    print 'is_login %s' %is_Login
    #如果is_Login参数是1， 跳转到问答页
    if is_Login == '1':
        return 'question 这是问答页'
    #如果参数是0，重定向到登陆页
    else:
        #获取到 login 方法的 url，
        url = url_for('login')
        #重定向到该url
        return redirect(url)

if __name__ == '__main__':
    app.run(debug = True)
