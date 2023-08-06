# -*- coding: utf-8 -*-
# @Time : 2022/3/9 1:33 下午
# @Author : chendb
# @Description : 工具集合


import yagmail
import json


def send_mail_util(from_user, pwd, host, to_user, subject, content):
    """
    发送邮件
    :param from_user: 发件人
    :param pwd: 密码
    :param host: 发件地址host
    :param to_user: 接收人
    :param subject: 邮件主题
    :param content: 邮件内容
    :return:
    """
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag.send(to_user, subject, content)

def json_util(pre_json, to_json_type, **kwargs):
    try:
        return json.loads(pre_json) if to_json_type == 'json_load' else json.dumps(
            pre_json, ensure_ascii=False, **kwargs)
    except:
        return pre_json