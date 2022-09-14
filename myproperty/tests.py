# – coding: gbk –
# import os,sys,json
import asyncio
import threading
from threading import Thread
import time
# import django.utils.timezone as timezone
# now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(now)

# notime = time.strftime('0000-00-00 00:00:00.000000', time.localtime(time.time()))
# print(notime)


# dict = {'csrfmiddlewaretoken': 'z1nvgyK7947z1roJ2TYFE9muVbsmr5UTtF7npiOzrTiHBCVJdbsTYZjfyaq0rzWg', 'userId': '2'}
# print(list(dict.items())[1])

# for i in dict.values():
#     print(i)
#
# dic = ('userId', '5')
# print(dic[1])
# print(timezone.now)

# a=1
# b=None
#
# print(a and b)
#
# if not a and b:
#     print('xx')
# else:
#     print('bb')
import os
from email.mime.text import MIMEText

# filepath = 'D:\\py\\djangoProject\\myproperty\\tes'

# with open(filepath, 'rb') as file:
#     att = MIMEText(file.read(), 'base64', 'utf-8')
#     att.add_header('Content-Type', 'application/octet-stream')
#     att.add_header('content-disposition', 'attachment', filename=os.path.basename(file.name))
#     print(file.read())


# f = ('D:\\py\\djangoProject\\myproperty\\tes', 'r')
# f = 'D:\\py\\djangoProject\\myproperty\\tes'
# # print(f.read())
#
# with open(f, 'rb') as file:
#     print(file.read())

# import json

# dictionary = {
#   "id": "04",
#   "name": "sunil",
#   "depatment": "HR"
# }
#
# json_object = json.dumps(dictionary)
#
# print(dictionary.values())
# pro_name = 'xsx'
# typed = '123'
# num = 4
# asset_code = 'ff'
# requisition_time = 'today'
#
# #
# if not (pro_name == 'xx' and typed and num and asset_code and requisition_time):
#     result = 0
#     print(result)
# else:
#     result = 1
#     print(result)
#
#
import requests
# url = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo'.format('WB09745642')
#
# # res = os.popen("curl -X GET -s -k https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo".format('WB09745642'))
# print(url)
# # res = os.popen("curl -X GET -s -k " + url)
# # print(res)
#
# code = requests.get(url).status_code
# print(code)
# data = eval(res.read())
# print(data)
# print(type(data['statusCode']))

# url2 = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo'.format('1232')
# res2 = os.popen("curl -X GET -s -k " + url2)
# data = eval(res2.read())
# print(data)
# print(type(data['statusCode']))

# while code == 200:
#     data = eval(res.read())
#     print(data)
#     if data['statusCode'] == '100201':
#         continue
#     elif data['statusCode'] == 200:
#         # warranty = data['data']['detailinfo']['warranty'][0]
#         # startdate = warranty['StartDate']
#         # endtdate = warranty['EndDate']
#
#         data = data['data']
#         print(data)
#
#         break
# else:
#     startdate = None
#     endtdate = None
# print(startdate)
# print(endtdate)


# url = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivewarrantyinfo'.format('PF3B0VT0')
# res = os.popen("curl -X GET -s -k https://newsupport.lenovo.com.cn/api/drive/{}/drivewarrantyinfo".format('PF3B0VT0'))
#
# code = requests.get(url).status_code
# # print(code)
#
# while code == 200:
#     data = eval(res.read())
#     # print(data)
#     # print(data['statusCode'])
#     # print(type(data['statusCode']))
#
#     if data['statusCode'] == '100':
#         startdate = None
#         endtdate = None
#         break
#     elif data['statusCode'] == 200:
#         warranty = data['data']['detailinfo']['warranty'][0]
#         startdate = warranty['StartDate']
#         endtdate = warranty['EndDate']
#         break
# else:
#     startdate = None
#     endtdate = None
# print(startdate)
# print(endtdate)

# print(code)
# if code == 200:
#     data = eval(res.read())
#     print(data)
#     print(data['statusCode'])
#     print(type(data['statusCode']))
#
#     if data['statusCode'] == '100':
#         breakpoint()
#     elif data['statusCode'] == 200:
#         warranty = data['data']['detailinfo']['warranty'][0]
#         startdate = warranty['StartDate']
#         endtdate = warranty['EndDate']
# else:
#     startdate = None
#     endtdate = None
# print(startdate)
# print(endtdate)


# url = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo'.format('PF3B0VT0')
# # res = os.popen("curl -X GET -s -k " + url)
# res = os.popen("curl -X GET -s -k https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo".format('PF3B0VT0'))
# code = requests.get(url).status_code
# print(code)
# while code == 200:
#     data = eval(res.read())
#     # print(type(data['statusCode']))
#     if data['statusCode'] == '100201':
#         model1 = None
#         model2 = None
#         break
#     elif data['statusCode'] == 200:
#         model1 = data['data'][0]['Data'][0]['Notes']
#         model2 = data['data'][0]['Data'][1]['Notes']
#
#         break
# else:
#     model1 = None
#     model2 = None


# class MyThread(threading.Thread):
#     def __init__(self):
#         super(MyThread, self).__init__()
#         self.mutex = threading.Lock()
#
#     def run(self):
#         self.mutex.acquire()
#         threading.Thread(target=runwjw).start()
#         self.mutex.release()
        # t1 = MyThread()
        # t1.run()


import hashlib
import schedule

# last_url = 'https://open.wenjuan.com/openapi/v4/get_latest_rspd_detail?app_key=' + app_key + '&timestamp='\
#     + str(timestamp) + '&short_id=' + short_id + '&signature=' + signature_hash
# print(last_url)
# res = requests.get(last_url)
# data = res.json()
# name = data['data']['Q1']['answer']
# sign = data['data']['Q3']['answer'][8:]
# print(name)
# print(sign)


# class GetWjw(object):
#     def __init__(self):
#         self.app_key = 'wjSbXPqOAxcM2mkhrt'
#         self.timestamp = round(time.time())
#         self.short_id = 'UZBZJvtQjf2'
#         self.app_secret = 'DmbO5w7qBQC2GR6Y3hvJerUN1Xu8Hxs0'
#
#     def run(self):
#         signature = self.app_key + self.short_id + str(self.timestamp) + self.app_secret
#         signature_hash = hashlib.md5(signature.encode(encoding='UTF-8')).hexdigest()
#         all_url = 'https://open.wenjuan.com/openapi/v4/get_rspd_list?app_key=' + self.app_key + '&timestamp=' \
#                   + str(self.timestamp) + '&short_id=' + self.short_id + '&signature=' + signature_hash
#         res = requests.get(all_url)
#         datas = res.json()
#         total_count = datas['data']['total_count']
#         return total_count, datas
#
#     @staticmethod
#     def getsign(now_count, datas):
#         last_data = datas['data']['rspd_list'][now_count:]
#         name_list = []
#         sign_list = []
#         for last in last_data:
#             name = last['Q1']['answer']
#             sign = last['Q3']['answer'][8:]
#             name_list.append(name)
#             sign_list.append(sign)
#         return name_list, sign_list


# if __name__ == '__main__':
#     count = GetWjw().run()[0]
#     wjw = GetWjw()
#     while count == GetWjw().run()[0]:
#         schedule.run_pending()
#         time.sleep(3)
#     data = GetWjw().run()[1]
#     data_tuple = wjw.getsign(count, data)






from multiprocessing import Process
# import time
# import math
# import queue
# import concurrent.futures
#
#
# class GetWjw(object):
#     def __init__(self):
#         self.app_key = 'wjSbXPqOAxcM2mkhrt'
#         self.timestamp = round(time.time())
#         self.short_id = 'UZBZJvtQjf2'
#         self.app_secret = 'DmbO5w7qBQC2GR6Y3hvJerUN1Xu8Hxs0'
#
#     def run(self, page):
#         page = str(page)
#         signature = self.app_key + page + self.short_id + str(self.timestamp) + self.app_secret
#         signature_hash = hashlib.md5(signature.encode(encoding='UTF-8')).hexdigest()
#         all_url = 'https://open.wenjuan.com/openapi/v4/get_rspd_list?app_key=' + self.app_key + '&timestamp=' \
#                   + str(self.timestamp) + '&page=' + page + '&short_id=' + self.short_id + \
#                   '&signature=' + signature_hash
#         res = requests.get(all_url)
#         datas = res.json()
#         total_count = datas['data']['total_count']
#         return total_count, datas
#
#     @staticmethod
#     def getsign(now_count, datas, page):
#         num = now_count - (page - 1)*20 - 1
#         last_data = datas['data']['rspd_list'][num:]
#         name_list = []
#         sign_list = []
#         for last in last_data:
#             name = last['Q1']['answer']
#             sign = last['Q3']['answer'][8:]
#             name_list.append(name)
#             sign_list.append(sign)
#         return name_list, sign_list
#
#
# def runwjw():
#     page = 1
#     count = GetWjw().run(page)[0]
#     wjw = GetWjw()
#     page = math.ceil(count / 20)
#     while count == GetWjw().run(page)[0]:
#         schedule.run_pending()
#         time.sleep(2)
#         break
#     data = GetWjw().run(page)[1]
#     wjw.getsign(count, data, page)
#     data_tuple = wjw.getsign(count, data, page)
#     print(data_tuple)
#     return data_tuple
#
#
# def pos():
#     # t1 = threading.Thread(target=runwjw)
#     # t1.start()
#
#     # pass
#     print('主进程')
# pos()


# def foo(arg):
#     return arg
#
#
# class ThreadWithReturnValue(Thread):
#     def run(self):
#         if self._target is not None:
#             self._return = self._target(*self._args, **self._kwargs)
#
#     def join(self):
#         super().join()
#         return self._return
#
#     def ret(self):
#         time.sleep(1)
#         return self._return
#
#
# twrv = ThreadWithReturnValue(target=foo, args=("hello world",))
# twrv.start()
# print(twrv.ret())
# print('xxx')


# class MyThread(threading.Thread):
#     def __init__(self):
#         super(MyThread, self).__init__()
#         self.mutex = threading.Lock()
#
#     def run(self):
#         self.mutex.acquire()
#         threading.Thread(target=runwjw).start()
#         self.mutex.release()
#
#
# t1 = MyThread()
# t1.run()
# print('主进程')
# import pymysql
# import sys
# import base64
# import io
# from PIL.Image import Image
# import os
#
# def dbinfo():
#     conn = ""
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user="root", password='123', db='infos',
#                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
#     cur = conn.cursor()
#     if not cur:
#         return "access db is fail!"
#     else:
#         return conn
#
# # fp = open('1.jpg','rb').read()
# # base64_date = base64.b64encode(fp)
#
# try:
#     conn = dbinfo()
#     conncur = conn.cursor()
#     sql_selectimage = "select * from infos.myproperty_user WHERE id=5"
#     conncur.execute(sql_selectimage)
#     softpath = conncur.fetchall()
#     softpathlist = [x['username'].decode('gbk') for x in softpath]
#     print(softpathlist)
#     for i in softpathlist:
#         print(i)
#         imgdata = base64.b64decode(i)
#         print(imgdata)
#         with open('123.png', 'wb') as f:
#             f.write(imgdata)
#
#     conn.commit()
#     conn.close()
#
# except pymysql.Error as e :
#     # print(e)
#     sys.exit(1)

# a = [{'title': '抬头', 'date': '2022'}, {'title': '抬头', 'date': '2021'}]
# for i in a:
#     print(i)
#     print(type(i))
#
# import datetime
from datetime import date
#
# print(date.today())
# print(date.today())

import chinese_calendar
from datetime import datetime as dt
import pandas as pd
import datetime

today = date.today()

# tendays_age = (today + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
twentydays_later = (today + datetime.timedelta(days=+34)).strftime("%Y-%m-%d")

# start_time = dt.strptime(str(tendays_age), '%Y-%m-%d')
end_time = dt.strptime(str(twentydays_later), '%Y-%m-%d')

# workdays = pd.DataFrame(chinese_calendar.get_workdays(today, end_time))
#
# # workdays = workdays.rename(columns={0: '日期'})
# # workdays['属性'] = '工作日'
# print(workdays)


# workdays = chinese_calendar.get_workdays(today, end_time)
# holidays = chinese_calendar.get_holidays(today, end_time)
# workdays_len = len(workdays)
#
# c = []
# a = []
# x = []
# for workday in workdays:
#     c.append(workday.strftime("%W"))
# for i in range(0, len(c)):
#     if i + 1 < len(c):
#         if c[i] == c[i + 1]:
#             x.append(c[i])
#         else:
#             x.append(c[i])
#             a.append(x)
#             x = []
#     else:
#         x.append(c[len(c) - 1])
#         a.append(x)
#
# num = []
# for i in a:
#     num.append(len(i))
# print(num)
#
# qy = int(c[0]) % 3
# if qy == 0:
#     user_list = ['胡少桂', '蒋晶欣', '刘轩']
# elif qy == 1:
#     user_list = ['蒋晶欣', '刘轩', '胡少桂']
# else:
#     user_list = ['刘轩', '胡少桂', '蒋晶欣']
#
# color = ['#7B68EE', '#378006', '#F4A460']
#
# x = 0
# for i in range(len(num)):
#     if len(num) > len(user_list):
#         user_list.append(user_list[x])
#         color.append(color[x])
#         x += 1
# print(user_list)
#
# new_list = []
# i = 0
# for user in user_list:
#     # print(num[user_list.index(user)])
#     # new_list += num[user_list.index(user)] * list(user.split())
#     new_list += num[i] * list(user.split())
#     i += 1
#
# j = 0
# new_color = []
# for col in color:
#     new_color += num[j] * list(col.split())
#     j += 1
#
# calendar_list = []
#
# # print(workdays)
# for i in range(len(workdays)):
#     dict1 = {'title': new_list[i], 'start': workdays[i], 'color': new_color[i]}
#     calendar_list.append(dict1)
# print(calendar_list)






