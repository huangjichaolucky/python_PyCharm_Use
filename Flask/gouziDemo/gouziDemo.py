# coding=utf-8
from flask import Flask, render_template, request, \
    session, url_for, redirect

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    print 'hello'
    return 'Hello World!'

@app.route('/login/', methods = ['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
        # return 'wowoow'
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '1':
            session['username'] = '1'

            return u'登陆成功'
        else:
            return u'登陆失败'

@app.route('/edit/')
def edit():
    if session.get('username'):
        return u'有人'
    else:
        print u'没登陆'
        return redirect(url_for('login'))
        # return render_template('login.html')


# 在请求之前执行的
# 是在视图函数执行之前执行的
# 这个函数只是一个装饰器，他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行
@app.before_request
def before_request_method():
    print 'before'


    # * 上下文处理器应该返回一个字典。字典中的`key`会被模板中当成变量来渲染。
    # * 上下文处理器中返回的字典，在所有页面中都是可用的。
    # * 被这个装饰器修饰的钩子函数，必须要返回一个字典，即使为空也要返回。

# @app.context_processor
# def context_processor_method():
#     # username = session.get('username')
#     # if username:
#     #     #  可将 该值返回出去，每个文件都能够访问到
#     #     return {'username': username}
#     return u'没人'


if __name__ == '__main__':
    app.run(debug=True)
