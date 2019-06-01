# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : task2.py
# @Software : PyCharm


import time
from celery_app import app


@app.task
def mult(x, y):
    time.sleep(15)
    return x * y
