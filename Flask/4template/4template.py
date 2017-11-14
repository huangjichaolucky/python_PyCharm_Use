#-*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
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
        'age' : 30,
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

if __name__ == '__main__':
    app.run(debug=True)
