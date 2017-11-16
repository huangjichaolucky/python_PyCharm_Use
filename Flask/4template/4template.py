#-*- coding=utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/helloWorld')
def hello_world():

    # return 'Hello World!'


    # 1 定向到模板的helloWorldHtm.htmll文件，模板文件存放在 `templates` 文件夹或子文件夹中下，
    # 若是在 `templates` 文件夹下，不用带 `templates` 文件夹路径，直接写文件名即可
    # 若是在其子文件夹下，需要带上子文件夹的路径
    # return render_template('helloWorldHtml.html')


    class Person(object):
        def __init__(self):
            self.name = 'personName'
            self.sex = u'女'

    p = Person()


    userInfo = {
        'username' : u'小明',
        'sex' : u'男',
        'age' : 50,
        'person': p,
        'tempDic': {
            't1':'t1Value',
            't2': 't2Value'
        }
    }

    # 2 若传一个参数、少量参数，可以直接传过去，
    # return render_template('helloWorldHtml.html', userName = u'荷兰')

    # 3若传递多个参数，可将多个参数放到字典中去，然后将字典转成关键参数传递过去，
    # 该字典中 的某个键 对应的值可以是基本类型、对象类型、字典类型均可
    return render_template('helloWorldHtml.html', **userInfo)

    # 4 在模板文件中如何使用if 语句，
    # 情景如下，年纪大于30在模板中显示  大叔， 年纪大于30
    # 若小于30，显示  小鲜肉
    # 详见 模板文件

# 访问 ifTest路径查看效果
@app.route('/ifTest/')
def ifTest():
    age = 30
    return render_template('ifTest.html', age = age)


#访问 forTest路径 查看效果
@app.route('/forTest/')
def forTest():
    booksDic = {
        'name' : u'好书',
        'price' : 20,
        'author' : u'好作者'
    }

    array = [
        1, 3, 4, 5
    ]
    return  render_template('forTest.html',
                            booksDic = booksDic, array = array)

class Book(object):
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

@app.route('/forDemo/')
def forDemo():

    b1 = Book(u'红楼梦', u'曹雪芹', 300)
    b2 = Book(u'三国演义', u'罗贯中', 200)
    b3 = Book(u'西游记', u'吴承恩', 330)
    b4 = Book(u'水浒传', u'施耐庵', 100)
    books = [
        b1, b2, b3, b4
    ]
    return  render_template('forDemo.html', books =books)


# 过滤器
@app.route('/filterTest/')
def filterTest():

    b1 = Book(u'红楼梦', u'曹雪芹', 300)
    b2 = Book(u'三国演义', u'罗贯中', 200)
    b3 = Book(u'西游记', u'吴承恩', 330)
    b4 = Book(u'水浒传', u'施耐庵', 100)
    books = [
        b1, b2, b3, b4
    ]
    avatar = 'https://www.baidu.com/img/bd_logo1.png'
    # return render_template('filterTest.html')
    return render_template('filterTest.html',avatar=avatar, books=books)

#基类视图
@app.route('/baseView/')
def baseView():
    return render_template('baseView.html')

#子类页面1
@app.route('/subView/')
def subView():
    return render_template('subView.html')

#子类页面2
@app.route('/subView2/')
def subView2():
    return render_template('subView2.html')

if __name__ == '__main__':
    app.run(debug=True)
