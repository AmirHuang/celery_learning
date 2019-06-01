# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : config.py
# @Software : PyCharm

import datetime
from celery.schedules import crontab
BROKER_URL = 'redis://localhost:6379/3'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/4'
CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

# 定时任务配置如下
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': datetime.timedelta(seconds=10),
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.mult',
        'schedule': crontab(hour=16, minute=32),
        'args': (4, 5)
    }
}

# 当有定时任务的时候 可以执行如下两条任务
# celery beat -A celery_app -l INFO   # 表示开始定时任务
# celery worker -A tasks -l INFO      # 表示执行任务 当没有定时任务的时候  也是执行这条

# 当有定时任务的时候  也可以执行一条命令
# celery -B -A celery_app worker -l INFO  # 好像window不行

# -B 表示 定时任务
# -A 表示 应用目录 应用app目录？ 当有多个应用的时候呢  这是一个问题
# -l 表示日志级别

