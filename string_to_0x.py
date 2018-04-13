#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:
# Filename:
# Author:
import binascii
print("编码转换HEX")
aa = input("请输入字符串:")
aa = binascii.b2a_hex(aa.encode("utf-8"))
print('0x%s' % aa.decode())
