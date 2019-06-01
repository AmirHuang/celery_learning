# _*_ coding: utf-8 _*_
# @time     : 2019/06/01
# @Author   : Amir
# @Site     : 
# @File     : app.py.py
# @Software : PyCharm

import datetime
from celery_app import task1
from celery_app import task2

start = datetime.datetime.now()
task1.add.delay(2, 4)
task2.mult.delay(4, 5)
end = datetime.datetime.now()
print(end - start)
print('end.....')
