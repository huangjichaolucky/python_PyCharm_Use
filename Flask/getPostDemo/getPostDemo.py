# coding=utf-8
from flask import Flask, render_template, request, g
from utils import login_log

app = Flask(__name__)
# 我就是我

@app.route('/')
def hello_world():
    print '我就是我 %s' %'www'
    return render_template('index.html')

@app.route('/search/')
def search():
    # 获取到网络请求的参数, 此处是 get请求
    print request.args
    print request.args.get('q')
    return 'search!'

# 默认的视图函数，使用get请求方式，若使用post请求，需实现声明
@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 获取到网络请求的参数, 此处是 post请求
        print request.form
        print '用户名'

        username = request.form.get('username')
        # g 可作为全局变量, 可直接给 g 变量添加属性，有点类似单例模式
        g.username = username
        print username

        login_log(username)
        return 'post 请求'

if __name__ == '__main__':
    app.run(debug=True)
