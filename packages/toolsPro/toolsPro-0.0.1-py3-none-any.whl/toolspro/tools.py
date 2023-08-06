# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:29 下午
# @Author : guhao
# @Description : 工具包

from .util import send_mail_util


class Tool(object):

    def __init__(self):
        self.mail_from_user = ''        # 发件人账号
        self.mail_from_user_pwd = ''    # 发件人密码
        self.mail_from_user_host = ''   # 邮件SMTP服务器地址

    def send_mail_msg(self, to_user, subject, content):
        """
        这里调用send_mail_util函数方法，对外实例化调用
        :param to_user:
        :param subject:
        :param content:
        :return:
        """
        send_mail_util(self.mail_from_user, self.mail_from_user_pwd, self.mail_from_user_host,
                       to_user, subject, content)
