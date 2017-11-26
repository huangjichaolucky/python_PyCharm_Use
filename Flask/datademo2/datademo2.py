#coding=utf-8
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


#用户表
class User(db.Model):
    __tablename__ = 'user'
    # 数据类型是  db.Integer， 做为主键用，自动增长
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # String 类型，字符长度不超过 100， 不能为空
    name = db.Column(db.String(100), nullable=False)

    #自定义 打印内容
    def __repr__(self):
        return '<User %r>' % (self.name)

#文章表
class Article(db.Model):
    __tablename__ = 'article'
    # id  映射到 model 当中， 需要用  db.Cloumn()来实现
    # 数据类型是  db.Integer， 做为主键用，自动增长
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #String 类型，字符长度不超过 100， 不能为空
    name = db.Column(db.String(100), nullable=False)
    #Text 类型，
    text = db.Column(db.Text, nullable=False)
    #引用 user表中的 id字段，外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #模型的名字，反向引用
    # author 对应 User表， User 对象通过articles属性可访问这个作者的所有文章
    author = db.relationship('User', backref=db.backref('articles'))

    def __repr__(self):
        return '<Article %r>' % (self.name)

db.create_all()

@app.route('/')
def hello_world():
    # 增
    # user1 = User(name='username1')
    # db.session.add(user1)
    # db.session.commit()

    # art1 = Article(name='article1', text='article1 text1', author_id='3')
    # db.session.add(art1)
    # db.session.commit()

    # art1 = Article(name='article1', text='article1 text1')
    # art1.author = user1
    # db.session.add(art1)
    # db.session.commit()

    #查找某个文章的作者
    # article = Article.query.filter(Article.name == 'article1').first()
    # print article.author.name

    # art2 = Article(name='article2', text='article2 text2', author_id='5')
    # db.session.add(art2)
    # db.session.commit()

    #查找某个用户下的所有文章
    user = User.query.filter(User.name == 'username1').first()
    print user.articles
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
