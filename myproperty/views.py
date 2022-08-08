import math
import re
import threading
import requests
import json
import os
import time
import base64
from mycelery.wjw.tasks import runwjw, getredis
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from myproperty.models import Info, Grant
# Create your views here.


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


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
#         # print(datas)
#         return total_count, datas
#
#     @staticmethod
#     def getsign(now_count, datas, page):
#         num = now_count - (page - 1)*20 - 1
#         last_data = datas['data']['rspd_list'][num:]
#         name_list = []
#         sign_list = []
#         for last in last_data:
#             # print(last)
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
#         time.sleep(3)
#         break
#     data = GetWjw().run(page)[1]
#     wjw.getsign(count, data, page)
#     data_tuple = wjw.getsign(count, data, page)
#     print(data_tuple)
    # return data_tuple


def index(request):
    return render(request, 'index.html', locals())


def navigation(request):
    return render(request, 'navigation.html', locals())


def infodata(request):
    if request.method == "GET":
        infos = Info.objects.all()
        total = infos.count()
        rows = list(infos.values())
        return JsonResponse({'total': total, 'rows': rows})

    else:
        return render(request, 'index.html')


def management(request):
    lists = []
    no_used = Info.objects.filter(current_user='').distinct()
    for i in no_used.values('pro_name'):
        lists.append(i.get('pro_name'))
    user_list = ['刘轩', '胡少桂', '蒋叶飞', '蒋晶欣', '张林', '王鑫']
    return render(request, 'management.html', locals())


# def findsearch(request):
#     # code = request.GET['code']
#     if request.method == "GET":
#         name = request.GET['name']
#         infos = Info.objects.filter(current_user=name)
#         total = infos.count()
#         rows = list(infos.values())
#         return JsonResponse({'total': total, 'rows': rows})
#
#     else:
#         return render(request, 'index.html')
    # return HttpResponse(json.dumps(name, cls=DateEncoder), content_type='application/json')


def showdata(request):
    # # global startdate, endtdate, model1, model2
    # datas = request.GET.dict()
    # # print(datas)
    # data = list(datas.items())[1]
    # # print(data)
    # i_d = data[1]
    i_d = request.GET['userId']
    pro_name = Info.objects.get(id=i_d).pro_name
    typed = Info.objects.get(id=i_d).type
    sn = Info.objects.get(id=i_d).sn
    num = Info.objects.get(id=i_d).num
    add_time = Info.objects.get(id=i_d).add_time
    asset_code = Info.objects.get(id=i_d).asset_code
    current_user = Info.objects.get(id=i_d).current_user
    requisition_time = Info.objects.get(id=i_d).requisition_time
    user_one = Info.objects.get(id=i_d).user_one
    # user_one_requisition_time = Info.objects.get(id=i_d).user_one_requisition_time
    remarks = Info.objects.get(id=i_d).remarks

    dic = {'pro_name': pro_name, 'type': typed, 'num': num, 'add_time': add_time, 'asset_code': asset_code,
           'current_user': current_user, 'requisition_time': requisition_time, 'user_one': user_one, 'sn': sn,
           'remarks': remarks}

    return HttpResponse(json.dumps(dic, cls=DateEncoder), content_type='application/json')


def findinfo(request):
    datas = request.GET.dict()
    data = list(datas.items())[1]
    i_d = data[1]
    sn = Info.objects.get(id=i_d).sn
    url = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivewarrantyinfo'.format(sn)
    data = requests.get(url).json()
    # res = os.popen("curl -X GET -s -k " + url)
    code = requests.get(url).status_code
    while code == 200:
        # data = eval(res.read())
        if data['statusCode'] == '100':
            startdate = None
            endtdate = None
            break
        elif data['statusCode'] == 200:
            warranty = data['data']['detailinfo']['warranty'][0]
            startdate = warranty['StartDate']
            endtdate = warranty['EndDate']
            break
    else:
        startdate = None
        endtdate = None

    url = 'https://newsupport.lenovo.com.cn/api/drive/{}/drivesetinginfo'.format(sn)
    data = requests.get(url).json()
    code = requests.get(url).status_code
    while code == 200:
        if data['statusCode'] == '100201':
            model1 = None
            model2 = None
            break
        elif data['statusCode'] == 200:
            model1 = data['data'][0]['Data'][0]['Notes']
            model2 = data['data'][0]['Data'][1]['Notes']
            break
    else:
        model1 = None
        model2 = None
    lenovo_info = 'CPU: ' + str(model1) + str(model2) + '\n' + '维保期: ' + str(startdate) + '————' + str(endtdate)
    dic = {'sn': sn, 'lenovo_info': lenovo_info}
    # print(dic)
    return HttpResponse(json.dumps(dic, cls=DateEncoder), content_type='application/json')
    # return render(request, 'management.html', locals())


@csrf_exempt
def saveinfo(request):
    i_d = request.POST.get('userId')
    current_user = Info.objects.get(id=i_d).current_user
    mytime = Info.objects.get(id=i_d).requisition_time
    # print(current_user)
    # sn = request.POST['sn']
    # print(sn)
    pro_name = request.POST.get('pro_name')
    typed = request.POST.get('type')
    num = request.POST.get('num')
    asset_code = request.POST.get('asset_code')
    new_current_user = request.POST.get('current_user')
    # print(new_current_user)
    # 空值-
    # nonetime = request.POST.get('requisition_time')
    # print(requisition_time)
    remarks = request.POST.get('remarks')
    # 判断当前使用者是否有值
    # 空
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # notime = time.strftime('1999-12-31 01:02:03', time.localtime(time.time()))

    if not current_user:
        Info.objects.filter(id=i_d).update(pro_name=pro_name, type=typed, num=num, asset_code=asset_code,
                                           current_user=new_current_user, remarks=remarks, requisition_time=None)
        if new_current_user:
            Info.objects.filter(id=i_d).update(requisition_time=now)

    else:
        Info.objects.filter(id=i_d).update(pro_name=pro_name, type=typed, num=num, asset_code=asset_code,
                                           current_user=new_current_user, remarks=remarks)
        if new_current_user != current_user:
            Info.objects.filter(id=i_d).update(current_user=new_current_user, requisition_time=now,
                                               user_one=current_user, return_date=now,
                                               user_one_requisition_time=mytime)
        if not new_current_user:
            Info.objects.filter(id=i_d).update(requisition_time=None)
        return HttpResponse(json.dumps(i_d), content_type='application/json')
    return HttpResponse(json.dumps(i_d), content_type='application/json')


def getlentype(request):
    sn = request.GET['sn']
    # print(sn)
    res = os.popen("curl -X GET -s -k https://newsupport.lenovo.com.cn/api/drive/drive_query?searchKey={}".format(sn))
    data = eval(res.read())
    if data['statusCode'] in ['200202', 422]:
        typed = request.POST.get('type')
        return HttpResponse(json.dumps(typed), content_type='application/json')
    else:
        typed = data['data'][0]['codeName']
        return HttpResponse(json.dumps(typed), content_type='application/json')


@csrf_exempt
def addinfo(request):
    # sn = request.POST['add_sn']

    # res = os.popen("curl -X GET -s -k https://newsupport.lenovo.com.cn/api/drive/drive_query?searchKey={}".format(sn))
    # data = eval(res.read())
    #
    # if data['statusCode'] in ['200202', 422]:
    #     typed = request.POST.get('type')
    #     # return HttpResponse(json.dumps(typed), content_type='application/json')
    # else:
    #     typed = data['data'][0]['codeName']

    typed = request.POST['type']
    pro_name = request.POST.get('pro_name')
    sn = request.POST.get('add_sn')
    # num = request.POST.get('num')
    remarks = request.POST.get('remarks')
    asset_code = request.POST.get('asset_code')
    objs = Info.objects.values_list('asset_code', flat=True)
    if asset_code in objs:
        result = 0
        return HttpResponse(json.dumps(result), content_type='application/json')
    current_user = request.POST.get('current_user')
    time1 = request.POST.get('dateTime')
    nonetime = request.POST.get('notime')
    requisition_time = request.POST.get('requisition_time')

    if not (pro_name and asset_code and time1):
        result = 0
        return HttpResponse(json.dumps(result), content_type='application/json')

    if not requisition_time:
        requisition_time = nonetime
    # Info.objects.create(pro_name='1112', type='1564', asset_code='D00921', add_time='2022-03-30 17:05:56',
    #                     user_one_requisition_time=nonetime, return_date=nonetime)
    Info.objects.create(pro_name=pro_name, type=typed, add_time=time1, asset_code=asset_code,
                        current_user=current_user, remarks=remarks, user_one_requisition_time=nonetime,
                        return_date=nonetime, requisition_time=requisition_time, sn=sn)
    result = 1
    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def selectinfo(request):
    type_list = []
    data = request.GET['selectinfo']
    objs = Info.objects.filter(current_user='').filter(pro_name=data)
    for obj in objs:
        type_list.append(obj.type)
    # print(type_list)
    type_list = list(set(type_list))
    return JsonResponse(type_list, safe=False)


def selectsn(request):
    code_list = []
    data = request.GET['selectinfo']
    objs = Info.objects.filter(current_user='').filter(type=data)
    for obj in objs:
        code_list.append(obj.asset_code)
    code_list = list(set(code_list))
    # print(code_list) 去重
    return JsonResponse(code_list, safe=False)


@csrf_exempt
def saveffbtn(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    code = request.POST['code']
    user = request.POST['user']
    infos = Info.objects.filter(asset_code=code).values()
    # print(infos)
    if code == '' or user == '请选择':
        result = 'fail'
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        for info in infos:
            info_id = info['id']
            name = info['pro_name']
            spec = info['type']
            sn = info['sn']

        # grant = Grant.objects.get(id=2)
        # name = grant.info.pro_name
        # spec = grant.info.type
        # sn = grant.info.sn
            Grant.objects.create(info_code=code, user_name=user, info_id=info_id, device=name, specification=spec,
                                 sn_num=sn, alters_date=now)
            Info.objects.filter(id=info_id).update(current_user=user, requisition_time=now)
        result = 'success'
        # runwjw.delay()
        task = runwjw.delay()
        # task_id = runwjw.delay().id
        task_id = task.id
        getredis.delay(task_id, user, code)
        return HttpResponse(json.dumps(result), content_type='application/json')


def selectrecover(request):
    parameter_list = []
    user = request.GET['select_user']
    objs = Info.objects.filter(current_user=user)
    for obj in objs:
        pro_name = obj.pro_name
        model = obj.type
        code = obj.asset_code
        parameter = pro_name + '(' + model + ')' + '-----' + code
        parameter_list.append(parameter)

    return JsonResponse(parameter_list, safe=False)


@csrf_exempt
def savehsbtn(request):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    result = request.POST['select']
    user = request.POST['user']
    code = re.findall(r"D\d+", result)
    # print(code)
    for i in code:
        req_time = Info.objects.get(asset_code=i).requisition_time
        Info.objects.filter(asset_code=i).update(current_user='', user_one_requisition_time=req_time,
                                                 requisition_time=None, user_one=user, return_date=now)

    return HttpResponse(json.dumps(code), content_type='application/json')


def workflow(request):

    return render(request, 'workflow.html', locals())


def grantdata(request):
    if request.method == "GET":
        objs = Grant.objects.defer('signature', 'info_id')
        total = objs.count()
        rows = list(objs.values('id', 'device', 'specification', 'user_name', 'info_code', 'alters_date'))
        return JsonResponse({'total': total, 'rows': rows})

    else:
        return render(request, 'index.html')


def showsign(request):
    i_d = request.GET['userId']
    obj = Grant.objects.get(id=i_d)
    user = obj.user_name
    img = obj.signature
    imgdata = base64.b64decode(img)
    with open('static/showsign/' + i_d + '.png', 'wb') as f:
        f.write(imgdata)
    # return render(request, 'workflow.html', locals())
    return HttpResponse(json.dumps(i_d), content_type='application/json')

