#-*- coding:utf-8 -*-
#从 flask 模块中导入  Flask类
from flask import Flask
import config

"""
初始化一个Flask对象
传递一个参数 __name__的用途：
    1. 方便flask框架去寻找资源
    2. 方便flask插件查找错误位置
"""
app = Flask(__name__)
app.config.from_object(config)
#app.route 是一个装饰器
# @ 开头，并且在函数的上面，，说明是一个装饰器
#这个 装饰器的作用： 做一个URL与视图函数的映射

#当访问127.0.0.0：5000/  时候，去请求hello_world函数，然后将返回结果返回给浏览器
@app.route('/')
# 视图函数
def hello_world():
    return 'Hello World 123456!'


#如果当前文件作为入口程序运行，那么就执行下面的语句，
# 即__name__ == '__main__'
# 若被作为模块引用，__name__ 就不是 '__main__'了
if __name__ == '__main__':
    #启动一个应用服务器，来接受用户请求
    # app.run()

    #设置成debug模式
    # 作用1 程序出现错误时，可以在页面中看到错误信息
    # 作用2 修改了项目中的Python文件，保存后，程序会自动加载，不用手动重启服务器
    # 方式1
    # app.run(debug=True)

    #方式2
    app.run()

# 设置debug模式的两种方式
# 1 新建一个 config.py文件
# 2 在主app文件中导入文件，并配置到app中
# 	即 import config
# 	app.config.from_object(config)
# 3 还有其他的参数，都放在这个配置文件中，比如数据库的配置 SECRET_KEY、SQLALCHEMY
#
# 第二种方式，直接在 主app文件中的设置为 run(debug = True)