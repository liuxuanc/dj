# – coding: gbk –
# import os,sys,json
# import time
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
pro_name = '刘轩'
typed = 'super'
num = 4
asset_code = 'nb'
requisition_time = 'today'
result = 2

if not (pro_name and typed and num and asset_code and requisition_time):
    result = 0
    print(result)
else:
    result = 1
    print(result)


a = 1
b = 2
if a != b:
    print(a)
else:
    print(b)

