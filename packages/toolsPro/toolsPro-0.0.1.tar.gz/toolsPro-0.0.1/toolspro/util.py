# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:25 下午
# @Author : guhao
# @Description : 工具包方法


import yagmail

def send_mail_util(from_user, pwd, host, to_user, subject, content):
    """
    发送邮件
    :param from_user: 发件人
    :param pwd: 发件人密码
    :param host: 邮箱SMTP HOST
    :param to_user: 收件人
    :param subject: 邮件主题
    :param content: 邮件内容
    :return:
    """
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag.send(to_user, subject, content)


