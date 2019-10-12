
# clery启动初始化，确保django项目启动时celery跟着启动
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

# 解决读取数据库问题加入下面两行
import pymysql
pymysql.install_as_MySQLdb()

#__all__ = ('celery_app',)
