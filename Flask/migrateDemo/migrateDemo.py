#-*- coding=utf-8 -*-

from flask import Flask
from exts import db
import config
# from models import Article    ----1--

app = Flask(__name__)
app.config.from_object(config)

#1 将 db变量放到单独的文件中去， 解决循环引用的问题， 那个文件中，初始化
# db变量时，没有用app变量，需在此处设置一下
db.init_app(app)

#3  不太明白， 使用迁移文件后即（manager文件），就不再使用下面两行代码了，
# 下面两行 代码和 ----1-- 处代码同时使用，若用 manager管理数据则不
# 用这两处代码
# 模型 映射到数据库中
# with app.app_context():
#     db.create_all()

#2 新建的model 模型，单独放到一个文件中去
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
