# coding:utf-8
'''
@File    : util.py
@Author  : guomin
@Desc    : 工具方法
'''

import yagmail

def send_mail_util(from_user,pwd,host,to_user,subject,content):
    """
    :param from_user:发件人
    :param pwd:发件人密码
    :param host:发件主机
    :param to_user:接收人
    :param subject:邮件主题
    :param content:邮件内容
    :return :

    """
    with yagmail.SMTP(user=from_user,password=pwd,host=host) as yag:
        yag.send(to_user,subject,content)


# 验证方法
if __name__=="__main__":
    send_mail_util("tech-tm-qa@pin-dao.cn","Tm-qa-888888","smtp.mxhichina.com","guomin1@pin-dao.cn","主题","你好呀内容")