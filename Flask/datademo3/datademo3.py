#-*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer,
                                 db.ForeignKey('article.id'),
                                 primary_key=True),
                       db.Column('tag_id', db.Integer,
                                 db.ForeignKey('tag.id'),
                                 primary_key=True)
                       )


#标签表
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<tag %r>' % (self.name)

#文章表
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    #最重要的一行代码
    tags = db.relationship('Tag', secondary=article_tag,
                           backref=db.backref('articles'))

    def __repr__(self):
        return '<Article %r>' % (self.name)

db.create_all()

@app.route('/')
def hello_world():
    # article1 = Article(name='aaa')
    # article2 = Article(name='bbb')
    #
    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')
    #
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    #
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # db.session.add(article1)
    # db.session.add(article2)
    #
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    # 查找 aaa 文章  对应的标签
    article1 = Article.query.filter(Article.name == 'aaa').first()
    tags = article1.tags
    for tag in tags:
        print tag.name

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
