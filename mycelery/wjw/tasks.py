from mycelery.main import app
from celery.result import AsyncResult
import time, datetime
import hashlib
import schedule
import math
import requests
import os
import pymysql
import sys
import base64


# backend = 'redis://127.0.0.1:6379/1'
# broker = 'redis://127.0.0.1:6379/3'
# cel = celery.Celery('test', backend=backend, broker=broker)


class GetWjw(object):
    def __init__(self):
        self.app_key = 'wjSbXPqOAxcM2mkhrt'
        self.timestamp = round(time.time())
        self.short_id = 'UZBZJvtQjf2'
        self.app_secret = 'DmbO5w7qBQC2GR6Y3hvJerUN1Xu8Hxs0'

    def run(self, page):
        page = str(page)
        signature = self.app_key + page + self.short_id + str(self.timestamp) + self.app_secret
        signature_hash = hashlib.md5(signature.encode(encoding='UTF-8')).hexdigest()
        all_url = 'https://open.wenjuan.com/openapi/v4/get_rspd_list?app_key=' + self.app_key + '&timestamp=' \
                  + str(self.timestamp) + '&page=' + page + '&short_id=' + self.short_id + \
                  '&signature=' + signature_hash
        res = requests.get(all_url)
        print(res)
        datas = res.json()
        total_count = datas['data']['total_count']
        return total_count, datas

    @staticmethod
    def getsign(now_count, datas, page):
        num = now_count - (page - 1)*20
        last_data = datas['data']['rspd_list'][num:]
        name_sign = {}
        for last in last_data:
            name = last['Q1']['answer']
            sign = last['Q3']['answer'][8:]
            name_sign[name] = sign
        return name_sign


@app.task
def runwjw():
    page = 1
    count = GetWjw().run(page)[0]
    wjw = GetWjw()
    page = math.ceil(count / 20)
    while count == GetWjw().run(page)[0]:
        schedule.run_pending()
        time.sleep(10)
        # break
    data = GetWjw().run(page)[1]
    data_tuple = wjw.getsign(count, data, page)
    return data_tuple


# @app.task
# def getlenovo():
#
#     pass


@app.task
def getredis(task_id, user, code):
    today = datetime.date.today()
    today = str(today) + '%'
    my_async = AsyncResult(id=task_id, app=app)
    while True:
        if my_async.successful():
            result = my_async.get()
            key_name = list(result.keys())[0]
            url = list(result.values())[0]
            res = requests.get(url=url)
            # localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            year = time.strftime('%Y', time.localtime(time.time()))
            month = time.strftime('%m', time.localtime(time.time()))
            path = os.getcwd()
            # E:\dj\mycelery\wjw
            p1 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
            # E:\dj\
            fileyear = 'E:/dj/static/signature/' + year
            filemonth = fileyear + '/' + month + '/'
            if not os.path.exists(fileyear):
                os.mkdir(fileyear)
                os.mkdir(filemonth)
            else:
                if not os.path.exists(filemonth):
                    os.mkdir(filemonth)
            if res.status_code == 200:
                open(filemonth + key_name + task_id + '.jpg', 'wb').write(res.content)
            # 判断分发时的人员与用户填写的名字是否相同，相同则保存到mysql中
            if user in result:
                for key, value in result.items():
                    if user == key:

                        def dbinfo():
                            conn = ""
                            conn = pymysql.connect(host='127.0.0.1', port=3306, user="root", password='123', db='infos',
                                                   charset='utf8', cursorclass=pymysql.cursors.DictCursor)
                            cur = conn.cursor()
                            if not cur:
                                return "access db is fail!"
                            else:
                                return conn

                        res = requests.get(value)
                        img = res.content
                        base64_date = base64.b64encode(img)
                        try:
                            conn = dbinfo()
                            conncur = conn.cursor()
                            sql_insertimage = """
                            update infos.grant set signature=%s where user_name=%s and alters_date LIKE %s"""
                            conncur.execute(sql_insertimage, (base64_date, user, today))
                            seatdic = conncur.fetchall()
                            conn.commit()
                            conn.close()

                        except pymysql.Error as e:
                            print("Error %d %s" % (e.args[0], e.args[1]))
                            sys.exit(1)

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
                        #         with open('1234.png', 'wb') as f:
                        #             f.write(imgdata)
                        #     conn.commit()
                        #     conn.close()
                        #
                        # except pymysql.Error as e:
                        #     print(e)
                        #     sys.exit(1)

            # break
            return 'ok'

        elif my_async.failed():
            print('faild')
        elif my_async.status == 'PENDING':
            print('PENDING')
        elif my_async.status == 'RETRY':
            print('RETRY')
        elif my_async.status == 'STARTED':
            print('STARTED')
        time.sleep(15)
    # return 'ok'


@app.task
def getlen():
    a = 'test'
    return a

