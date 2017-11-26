#-*- coding=utf-8 -*-
from exts import db
#文章表
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Article %r>' % (self.name)