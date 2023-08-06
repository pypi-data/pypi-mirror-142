# @Time    : 2022/3/15 7:15 下午 
# @Author  : yangxy
# @File    : util.py 
# @Desc    :
# @Software: PyCharm

import yagmail

def send_mail_util(from_user, pwd, host, to_user, subject, content):
    """

    :param from_user:
    :param pwd:
    :param host:
    :param to_user:
    :param subject:
    :param content:
    :return:
    """
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag.send(to_user, subject, content)


if __name__ == "__main__":
    send_mail_util()