#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:一个登录接口
# Author:smelond
import os

username = "smelond"  # 用户名
password = "qweqwe"  # 密码
counter = 0  # 计数器

# 读取黑名单
file = os.path.exists("./user.txt")  # 检查当前目录是否有user.txt这个文件，如果有者输出True赋给file
if file == True:  # 判断是否有user.txt这个文件
    blacklist_file = open("user.txt", "r").read()  # open()打开文件，并且用read()读取文件,然后赋给blacklist_file
    if blacklist_file == username:  # 检查文件里面的内容是否和我们的用户名相等
        print("Username lock. Please contact the administrator to remove the restrictions!!!")  # 输出错误提示
        exit()  # 退出程序

# 登录接口
for i in range(3):
    counter += 1  # 对每次登录进行计数
    input_user = input("Please input username: ")
    input_pass = input("Please input password: ")
    if input_user == username and input_pass == password:
        print("Welcome login...")
        break
    else:
        print("ERROR Incorrect username or password!!!")
        continue

# 写入黑名单
if counter == 3:  # 判断我是否输入错误三次
    print("The user name has been disabled")  # 提示信息
    blacklist_user = open("user.txt", "a")  # 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
    blacklist_user.write("%s" % username)  # 将用户名写入黑名单
    blacklist_user.close()  # 使用open后一定要记得调用文件对象的close()方法
