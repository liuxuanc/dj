import re
import requests
import json
import os
import time
from datetime import date
import base64
from mycelery.wjw.tasks import runwjw, getredis
import chinese_calendar
import datetime
from datetime import datetime as dt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from myproperty.models import Info, Grant
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('myproperty:login'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('myproperty:index'))
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # request.session['is_login'] = True
            # request.session['user_name'] = username
            # return render(request, 'index.html', {'username': username})
            return redirect(reverse('myproperty:index'))
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


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


@login_required(login_url='myproperty:login')
@permission_required('myproperty.add_info', raise_exception=True)
def management(request):
    lists = []
    no_used = Info.objects.filter(current_user='').distinct()
    for i in no_used.values('pro_name'):
        lists.append(i.get('pro_name'))
    user_list = ['刘轩', '胡少桂', '蒋叶飞', '蒋晶欣', '张林', '王鑫']
    return render(request, 'management.html', locals())


def showdata(request):
    # # global startdate, endtdate, model1, model2
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
    print(time1)

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
    data = request.GET['selectinfo']
    objs = Info.objects.filter(current_user='').filter(type=data)
    code_list = []
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
    # print(parameter_list)
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
    # user = obj.user_name
    img = obj.signature
    imgdata = base64.b64decode(img)
    with open('static/showsign/' + i_d + '.png', 'wb') as f:
        f.write(imgdata)
    # return render(request, 'workflow.html', locals())
    return HttpResponse(json.dumps(i_d), content_type='application/json')


def calendar(request):
    today = date.today()
    twentydays_later = (today + datetime.timedelta(days=+24)).strftime("%Y-%m-%d")
    end_time = dt.strptime(str(twentydays_later), '%Y-%m-%d')
    workdays = chinese_calendar.get_workdays(today, end_time)
    c = []
    a = []
    x = []
    for workday in workdays:
        c.append(workday.strftime("%W"))
    for i in range(0, len(c)):
        if i + 1 < len(c):
            if c[i] == c[i + 1]:
                x.append(c[i])
            else:
                x.append(c[i])
                a.append(x)
                x = []
        else:
            x.append(c[len(c) - 1])
            a.append(x)
    num = []
    for i in a:
        num.append(len(i))

    qy = int(c[0]) % 3
    if qy == 0:
        user_list = ['胡少桂', '蒋晶欣', '刘轩']
        color = ['#378006', '#4169E1', '#F4A460']
    elif qy == 1:
        user_list = ['蒋晶欣', '刘轩', '胡少桂']
        color = ['#4169E1', '#F4A460', '#378006']
    else:
        user_list = ['刘轩', '胡少桂', '蒋晶欣']
        color = ['#F4A460', '#378006', '#4169E1']
    x = 0
    for i in range(len(num)):
        if len(num) > len(user_list):
            user_list.append(user_list[x])
            color.append(color[x])
            x += 1
    j = 0
    new_color = []
    for col in color:
        new_color += num[j] * list(col.split())
        j += 1
    new_list = []
    i = 0
    for user in user_list:
        new_list += num[i] * list(user.split())
        i += 1
    calendar_list = []
    for i in range(len(workdays)):
        dict1 = {'title': new_list[i], 'start': workdays[i], 'color': new_color[i]}
        calendar_list.append(dict1)
    return JsonResponse(calendar_list, safe=False)
