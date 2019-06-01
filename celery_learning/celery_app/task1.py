# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : task1.py
# @Software : PyCharm


import time
from celery_app import app


@app.task
def add(x, y):
    time.sleep(30)
    return x + y
