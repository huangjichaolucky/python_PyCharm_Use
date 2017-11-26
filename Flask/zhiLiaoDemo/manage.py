# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zhiLiaoDemo import app
from exts import db


manager = Manager(app)

# 使用Migrate绑定app， db
migrate = Migrate(app, db=db)

# 添加迁移命令的脚本到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()