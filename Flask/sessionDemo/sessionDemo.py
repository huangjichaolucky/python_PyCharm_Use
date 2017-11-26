#coding=utf-8
from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
#24位的字符串
#随机24位的随机字符串  0-9 a-z A-Z
app.config['SECRET_KEY'] = os.urandom(24)

# 当session.permanent = True时，下行代码设置过期时间为7天，若不设置
# 过期时间，就默认是一个月过期
app.config['PERMAMENT_SESSION_LIFETIME'] = timedelta(days=7)

#设置session
@app.route('/')
def hello_world():
    # 操作session中
    # 和操作 字典是一样的
    session['username'] = 'huangjic'
    #  默认的过期时间是，关闭浏览器就过期
    # permanent = True 设置过期时间为一个月
    session.permanent = True
    return 'Hello World!'

#获取session
@app.route('/get/')
def getsessionM():
    # 两种取的操作，第一种会因为找不到 username，产生异常
    # 第二种方式，若找不到username 不会报错
    # session['username']
    # session.get('username')
    return session.get('username')

#删除session
@app.route('/delete/')
def delSessionM():
    print session.get('username')
    #删除session中的 username
    session.pop('username')
    #删除session中的所有数据
    # session.clear()
    print session.get('username')
    return '删除username'

if __name__ == '__main__':
    app.run(debug=True)
