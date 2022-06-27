#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 13:33
# @Author  : shaogui.hu
# @Site    :
# @File    : Email.py
# @Software: PyCharm

import time
import os, sys
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email.mime.multipart import MIMEMultipart
from PIL import Image
import config
import logging


class Mail_Basic:
    def __init__(self, host, port, username, password, subject, to: tuple, fromuser=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.subject = subject
        self.to = to

        self.msg = MIMEMultipart()
        self.msg['From'] = fromuser or username
        self.msg['To'] = ','.join(to)
        self.msg['Subject'] = Header(subject, 'utf-8')

    def text(self, text):
        """邮件正文 文本格式"""
        logging.debug(f"set email text: {text}")
        message = MIMEText(text, _subtype='plain', _charset='utf-8')
        self.msg.attach(message)
        return self

    def html(self, html):
        """邮件正文 HTML格式"""
        logging.debug("set email html: %s" % html)
        message = MIMEText(html, _subtype='html', _charset='utf-8')
        self.msg.attach(message)
        return self

    def addimage(self, filepath, width=None, height=None, X=1):
        """正文中添加图片"""
        logging.debug("set email addimage: %s" % filepath)
        self.html(
            self.imagehtml(filepath, width=width, height=height, X=X)
        )
        return self

    def imagehtml(self, filepath, width=None, height=None, X=1):
        """生成图片引用"""
        img = Image.open(filepath)
        with open(filepath, 'rb') as file:
            data = base64.b64encode(file.read()).decode()
            return '<img src="data:image/{img};base64,{data}" alt="{file_name}" width={width} height={height}>'.format(
                img=img.format, data=data, file_name=file.name,
                width=(width or img.width) * X, height=(height or img.height) * X
            )

    def add_file(self, filepath):
        """添加附件"""
        logging.info("set email add_file: %s" % filepath)
        with open(filepath, 'rb') as file:
            # att = MIMEText(file.read(), 'plain', 'utf-8')
            att = MIMEText(file.read(), 'base64', 'utf-8')
            att.add_header('Content-Type', 'application/octet-stream')
            att.add_header('content-disposition', 'attachment', filename=os.path.basename(file.name))
            self.msg.attach(att)

        return self

    def send(self):
        smtpObj = smtplib.SMTP_SSL(self.host, self.port)
        smtpObj.connect(self.host)
        smtpObj.login(self.username, self.password)
        smtpObj.sendmail(self.username, self.to, self.msg.as_string())
        smtpObj.quit()
        logging.info("send email subject: {subject} to: {to}".format(subject=self.subject, to=self.to))


class Mail(Mail_Basic):
    def __init__(self):
        super(Mail, self).__init__(
            host='smtp.qiye.aliyun.com',
            port=465,
            username='liu_xuan@gov-info.cn',
            password='Lx941026',
            subject='脚本运行结果',
            to=('15995502002@163.com', 'liu_xuan@gov-info.cn,'),
            # fromuser=config.EMAIL_FROMUSER
        )


if __name__ == '__main__':
    # subject = sys.argv[1]
    # html_file = sys.argv[2]
    # with open(html_file, 'r', encoding='utf-8') as file:

    # Mail().text('如附件所示').add_file('D:\\py\\djangoProject\\myproperty\\tes').add_file('D:\\py\\djangoProject\\myproperty\\tesx').send()
    # Mail().text('如附件所示').send()
    Mail().text('如附件所示').add_file('D:\\py\\djangoProject\\myproperty\\tes').send()

