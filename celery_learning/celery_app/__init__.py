# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : __init__.py.py
# @Software : PyCharm


from celery import Celery


app = Celery('demo')

app.config_from_object('celery_app.config')