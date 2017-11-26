#-*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
#dialect+driver://username:password@host:port/database

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/datademo'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    #定义表的名字
    __tablename__ = 'article'
    #id  映射到 model 当中， 需要用  db.Cloumn()来实现
    #数据类型是  db.Integer， 做为主键用，自动增长
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #String 类型，字符长度不超过 100， 不能为空
    name = db.Column(db.String(100), nullable=False)
    #Text 类型，
    text = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    #增
    #art1 = Article(name='article1', text='article1 text1')
    #db.session.add(art1)
    # db.session.commit()

    #增
    #art2 = Article(name='article2', text='article1 text2')
    #db.session.add(art2)
    # db.session.commit()

    #查
    # result = Article.query.filter(Article.name == 'article1').all()
    # print result[0].name

    #改
    #1 查找
    #2 改
    #3 提交
    #result1 = Article.query.filter(Article.name == 'article1').first()
    #result1.name = 'new article1'
    #db.session.commit()

    #删
    #1 查
    #2 删
    # 提交
    #result2 = Article.query.filter(Article.name == 'article2').first()
    #db.session.delete(result2)
    #db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
