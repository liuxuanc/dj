import json
import time
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from myproperty.models import Info
# Create your views here.


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
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


def management(request):
    return render(request, 'management.html')


def showdata(request):
    datas = request.GET.dict()
    # print(datas)
    data = list(datas.items())[1]
    # print(data)
    i_d = data[1]
    # print(i_d)
    # for k in datas:
    #     i_d = datas[k]

    pro_name = Info.objects.get(id=i_d).pro_name
    typed = Info.objects.get(id=i_d).type
    num = Info.objects.get(id=i_d).num
    add_time = Info.objects.get(id=i_d).add_time
    asset_code = Info.objects.get(id=i_d).asset_code
    current_user = Info.objects.get(id=i_d).current_user
    requisition_time = Info.objects.get(id=i_d).requisition_time
    user_one = Info.objects.get(id=i_d).user_one
    # user_one_requisition_time = Info.objects.get(id=i_d).user_one_requisition_time
    remarks = Info.objects.get(id=i_d).remarks

    dic = {'pro_name': pro_name, 'type': typed, 'num': num, 'add_time': add_time, 'asset_code': asset_code,
           'current_user': current_user, 'requisition_time': requisition_time, 'user_one': user_one,
           'remarks': remarks}

    return HttpResponse(json.dumps(dic, cls=DateEncoder), content_type='application/json')


@csrf_exempt
def saveinfo(request):
    i_d = request.POST.get('userId')
    current_user = Info.objects.get(id=i_d).current_user
    mytime = Info.objects.get(id=i_d).requisition_time
    # print(current_user)

    pro_name = request.POST.get('pro_name')
    typed = request.POST.get('type')
    num = request.POST.get('num')
    asset_code = request.POST.get('asset_code')
    new_current_user = request.POST.get('current_user')
    # print(new_current_user)
    # 空值-
    nonetime = request.POST.get('requisition_time')
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


@csrf_exempt
def addinfo(request):
    pro_name = request.POST.get('pro_name')
    typed = request.POST.get('type')
    num = request.POST.get('num')
    remarks = request.POST.get('remarks')
    asset_code = request.POST.get('asset_code')
    current_user = request.POST.get('current_user')
    time1 = request.POST.get('dateTime')
    nonetime = request.POST.get('notime')
    requisition_time = request.POST.get('requisition_time')

    if not (pro_name and typed and num and asset_code and time1):
        result = 0
        return HttpResponse(json.dumps(result), content_type='application/json')

    if not requisition_time:
        requisition_time = nonetime
    # Info.objects.create(pro_name='1112', type='1564', asset_code='D00921', add_time='2022-03-30 17:05:56',
    #                     user_one_requisition_time=nonetime, return_date=nonetime)
    Info.objects.create(pro_name=pro_name, type=typed, num=num, add_time=time1, asset_code=asset_code,
                        current_user=current_user, remarks=remarks, user_one_requisition_time=nonetime,
                        return_date=nonetime, requisition_time=requisition_time)
    result = 1
    # return render(request, 'management.html')
    return HttpResponse(json.dumps(result), content_type='application/json')
