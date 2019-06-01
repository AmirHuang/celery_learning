# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : task.py
# @Software : PyCharm
import time
from celery import Celery

broker = 'redis://localhost:6379/3'
backend = 'redis://localhost:6379/4'
app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print('---')
    time.sleep(500)
    return x + y


# celery worker -A tasks -l INFO
