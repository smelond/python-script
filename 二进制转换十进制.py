#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:
# Filename:
# Author:
print("IP地址转换【点分二进制转十进制】按CTRL+C退出")
while True:
    jieshou_ip = input("\n请输入二进制的IP地址:")
    for line in jieshou_ip.split("."):
        print("%s." % int(line, 2), end="")
