#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:用户管理程序，装饰器版本，多功能
# Filename:user_manage_program.py
# Author:smelond
# 程序有很多不足之处，比如很多地方能用装饰器，包括双层装饰器，很多地方需要优化,重复代码太多

import os

os.system("cls")  # windows中的清屏

COUNT = 0  # 计数器
WHETHER_LOGIN = {"is_login": "error"}  # 用于判断是否有用户登录
USER_LIST = []  # 当前用户信息存放的列表


def register_function():  # 注册函数 （所有注册都来调用这个函数）
    count = 3  # 计数器，做到了一个提示用户的作用
    for i in range(3):  # 循环3次
        print("用户注册【你只有3次机会】，你还有【%s】次机会".center(80, "=") % count)  # 输出提示
        count -= 1  # 每次减1
        username = input("请输入用户名：")
        while True:
            passwd = input("请输入密码：")
            if len(passwd) >= 5:
                break
            else:  # 如果输入的密码小于5,位数，向下操作
                print("请输入大于5位数的密码")
                input_passwd = input("【1：继续输入；2：返回上一步】")
                if input_passwd == "1":
                    pass
                else:
                    main()
        while True:
            email = input("请输入邮箱：")
            email_count = email.count("@")  # 查看输入的邮箱是否带@,
            # print(email_count)  # 返回1代表有一个@
            if email_count == 1:
                break  # 如果有一个@符号，代表邮箱输入正确，跳出当前循环
            else:
                print("请输入正确的邮箱")
                input_email = input("【1：继续输入；2：返回上一步】")
                if input_email == "1":
                    pass
                else:
                    main()

        register_user = [username, passwd, email, "2"]  # 将我们输入的用户名密码以及邮箱放到一个列表中，普通用户，所以加上了一个2
        with open("user.txt", "r") as user:
            for line in user:
                f_user_list = line.strip("\n").split("|")
                if register_user[0] == f_user_list[0]:
                    print("用户名已被注册")
                    break
                if register_user[2] == f_user_list[2]:  # 判断我们输入得的邮箱和用户名是否以及存在
                    print("邮箱已被注册")
                    break
            else:  # 接下来是通过了上面的筛选，开始把我们的注册信息写进数据库（总感觉上面有bug）
                user_write = "|".join(register_user)  # 用join方法将这个列表转换为以|分隔
                # open_user = open("user.txt", "a")  # a 以追加方式写入文件
                # open_user.write("\n" + user_write)
                # open_user.close()  # 记得关闭
                with open("user.txt", "a") as f:
                    f.write("\n" + user_write)  # 跟上面一样的方法，这种不用关闭文件
                print("注册成功")
                user_write = """用户名：【%s】;密码：【%s】;邮箱：【%s】""" \
                             % (register_user[0], register_user[1], register_user[2])  # 注册成功的提示信息
                return user_write  # 返回提示信息


def outer(func):  # 装饰器，用于管理接口
    def inner(*args, **kwargs):
        if WHETHER_LOGIN["is_login"] == "success" and USER_LIST[3] == "1":  # 为什么要加上引号，因为在列表中存储的是字符串，而不是整形
            r = func()  # 执行我们传入的函数
            return r  # 返回
        elif WHETHER_LOGIN["is_login"] == "success" and USER_LIST[3] == "2":  # 如果为普通用户，提示没有足够权限并且返回到main函数
            print("\n当前用户为普通用户【%s】，没有足够的权限" % USER_LIST[0])
            main()
        else:
            print("\n当前没有用户登录,请登录后再试。。。")  # 否者就是没有登录了
            main()

    return inner


def user_login(func):  # 检测用户是否登录的装饰器
    def inner(*args, **kwargs):
        if WHETHER_LOGIN["is_login"] == "success":  # 判断是否登录
            r = func()
            return r  # 如果已经登录，返回到原本的函数
        else:
            user_no = input("请登录后再试【1：用户登录；2：返回】:")
            if user_no == "1":
                login()
            else:
                print("返回成功")
                main()

    return inner  # 切记，这里必须返回一个inner，不然上面的inner不会执行,不能再后面加()，如果加上了，就相当于调用这个函数


def exit_login():  # 6退出登录
    global USER_LIST
    if USER_LIST:
        quit_login = input("当前用户为【%s】，确定要退出【Y/N】：" % USER_LIST[0])
        # if quit_login == "Y" or quit_login == "y" or quit_login == "yes":
        if quit_login in ("Y", "y", "yes", "yES", "yeS", "yEs", "YES", "Yes", "YEs"):  # 如果quit_login满足其中一个，继续执行
            WHETHER_LOGIN["is_login"] = "error"
            USER_LIST = []  # 直接将列表清除为初始状态，不知道这种方法好不好，但是好像管用
        elif quit_login in ("N", "n", "No", "nO", "NO"):
            print("退出失败")
    else:
        print("没有用户登录。。。")


def verifi_passwd():
    with open("user.txt", "r") as old_user:
        lines = old_user.readlines()  # 一次性读取整个文件，感觉这方方式不好
    flag = True
    cout = 3
    while flag:
        cout -= 1
        user_info = input("请输入用户名：")
        if user_info == "":  # 判断是否输入字符串
            print("你没有输入任何用户。。。\n")
            manage()
        for line in lines:
            user_all_info = line.strip("\n").split("|")
            if user_info == user_all_info[0]:
                current_user = user_all_info  # 如果输入的用户和用户文件里面的用户相同，那就将他的所有信息写入一个新的列表中
                flag = False
        if cout == 0:
            print("然而，你可能不知道有哪些用户，赶紧去查看吧。。。")
            manage()

    lines_user = [lines, current_user]
    return lines_user


def user_info_func(username, password_or_power, user_info, lines):  # 几个传入的类型为：用户名、密码或用户权限，需要修改的用户列表的位置、需要循环的文件内容
    new_user_info = username.copy()  # 将username复制给new_user_info
    new_user_info[user_info] = password_or_power  # 将新的用户密码修改为输入的新密码
    username = "|".join(username)  # 将列表转换为数据库可以识别的内容
    new_user_info = "|".join(new_user_info)
    # print(username, new_user_info)
    with open("user.txt", "w") as new_user:
        for line in lines:  # 将返回的整个文件循环打印
            if username in line:  # 如果返回的用户信息在返回的文件里面
                line = line.replace(username, new_user_info)  # 那就将旧的用户信息替换为新的用户信息
            new_user.write(line)  # 写入文件
        print("修改成功")  # 提示信息


@outer  # 调用装饰器
def manage():  # 5用户管理接口
    while True:
        print("用户管理接口【欢迎管理员[%s]】".center(69, "=") % USER_LIST[0])
        print("1：查看所有用户；2、添加新用户；3：删除用户；4：修改用户密码；5：升级用户权限；6：退出用户管理")
        user_input = input("请输入对象序号：")
        if user_input == "1":  # 查看用户信息
            print("\n" + "-" * 80)  # 打印80个-
            with open("user.txt", "r") as user_info:
                for line in user_info:
                    user_list = line.strip("\n").split("|")  # 去掉默认的\n和|将他转换为列表类型
                    if user_list[3] == "1":
                        user_rights = "管理员用户"  # 用户最后一个数如果等于1，代表管理员
                    else:
                        user_rights = "普通用户"  # 否者为普通用户
                    ordinary_user = """用户名【%s】\t密码【%s】\t邮箱【%s】\t用户等级【%s】""" \
                                    % (user_list[0], user_list[1], user_list[2], user_rights)  # 中间默认有一个换行符
                    print(ordinary_user)
            print("-" * 80 + "\n")

        elif user_input == "2":
            while True:
                ret = register_function()  # 调用注册函数
                print(ret)  # 输出返回值
                break  # 跳出当前这个while循环

        elif user_input == "3":
            flag = "error"  # 默认是没有用户的（做到一个提示作用）
            del_user = verifi_passwd()[1][0]  # 得到函数返回的第二个值
            print("\033[1;31m删除用户为：\033[0m", del_user)
            with open("user.txt", "r") as old_user:
                lines = old_user.readlines()  # 一次性读取整个文件，感觉这方方式不好1
            with open("user.txt", "w") as new_user:
                for line in lines:  # 将上面读取到的文集一行一行的循环出来
                    if line.startswith(del_user):  # 检查数据库里面是否有我们输入的用户（以输入的用户名开头）
                        flag = "success"
                        continue
                    new_user.write(line)
                if flag == "success":  # 提示成功
                    print("删除成功")
                else:
                    print("没有这个用户。。。")  # 如果输入的为空格或一些没有的用户，提示没有这个用户
                    continue

        elif user_input == "4":
            ret = verifi_passwd()  # 得到函数返回值
            lines = ret[0]  # 获取到返回的整个文件内容
            username = ret[1]  # 获取到返回的需要修改密码的用户
            new_password = input("请输入用户的新密码：")
            if len(new_password) < 5:  # 判断输入的密码长度是否大于或等于5位数
                error_prompt = input("你输入的密码长度小于5位数，由于你是管理员，输入Y继续：").strip("")  # 去掉输入的空格
                if error_prompt not in ("y", "Y"):  # 如果输入的值不为y或Y，就直接退出
                    print("退出。。。")
                    continue
            user_info_func(username, new_password, 1, lines)  # 传入实参到函数，1在列表中的位置代表用户的新密码
        elif user_input == "5":  # 下面这部分和上面的部分基本相似，其实可以写一个函数用来调用的
            ret = verifi_passwd()
            lines = ret[0]
            username = ret[1]  # 获取到输入用户的所有信息
            new_power = input("输入Y提升用户权限：")
            if new_power not in ("y", "Y"):
                print("输入错误。。。")
                break
            user_info_func(username, "1", 3, lines)  # 传入实参：用户名、权限（1代表管理员）、位置、循环的文件内容
        elif user_input == "6":
            print("返回上一级！！！")
            main()
        else:
            print("输入有误")


@user_login  # 调用装饰器
def see():  # 4查询当前用户的基本信息
    if USER_LIST[3] == "1":  # 数据库里面定义了1代表管理员用户，2代表普通用户
        user_level = "管理员用户"
    else:
        user_level = "普通用户"
    user_see = """
    ----------------------------------------
    用户名：  【%s】
    密  码：  【%s】
    邮  箱：  【%s】
    用户等级：【%s】
    ----------------------------------------
        """ % (USER_LIST[0], USER_LIST[1], USER_LIST[2], user_level)  # 一个简单的格式化输出
    print(user_see)


def error_password():
    counter = 3
    while True:
        counter -= 1
        if counter == 0:
            print("你输入错误的次数太多，程序自动返回。。。")
            main()
        else:
            print("两次输入的密码不相同。。。")
            continue


@user_login  # 调用装饰器
def alter():  # 3修改密码
    print("当前用户为：【%s】" % USER_LIST[0])
    while True:
        old_user_password = input("请输入当前用户的旧密码密码：")
        if old_user_password == USER_LIST[1]:
            flag = True
            count = 3
            while flag:
                count -= 1
                new_user_password = input("请输入当前用户的\033[1;31m新密码\033[0m：")  # 给新密码字体加颜色
                new_user_password1 = input("再次输入当前用户的\033[1;31m新密码\033[0m：")
                if len(new_user_password) >= 5:
                    flag = False
                elif count == 0:
                    print("多次不合法，程序自动返回。。。")
                    main()
                else:
                    print("输入不合法，请输入大于5位数的密码")
            if new_user_password == new_user_password1:  # 判断两次输入的密码是否相等
                with open("user.txt", "r") as user_info:  # 以读的方式打开这个文件
                    old_user_info = "|".join(USER_LIST)  # 获取以前的旧信息
                    for line in user_info:  # 将获取到的每行循环输出
                        if USER_LIST[0] in line:  # 找到当前登录的用户的这个用户名
                            USER_LIST[1] = new_user_password1  # 如果找到了，就把新密码重新加入到我们全局的用户的信息列表中
                            new_user_info = "|".join(USER_LIST)  # 将用户信息表中的内容用join方法转换为用户数据库里面的格式（新用户信息）
                            # print(new_user_info)
                            # print(old_user_info)
                            break  # 跳出当前
                with open("user.txt", "r") as old_user:
                    lines = old_user.readlines()  # 一次性读取整个文件，感觉这方方式不好
                with open("user.txt", "w") as new_user:
                    for line in lines:  # 将上面读取到的文集一行一行的循环出来
                        if old_user_info in line:  # 检查文件里面是否有我们用户的旧信息
                            line = line.replace(old_user_info, new_user_info)  # 如果有就用replace替换
                        new_user.write(line)  # 接着写入到文件
                print("修改成功√")
                break  # 完成后跳出

            else:  # 两次不相等
                print("两次输入的密码不相同，程序自动返回。。。")
                main()
        else:  # 当前用户密码输入错误
            print("当前用户密码输入错误，程序自动返回。。。")
            main()


def register():  # 2用户注册
    if WHETHER_LOGIN["is_login"] == "success":
        quit_login = input("无法注册用户，请退出登录后重试【1：退出登录；2：返回上一步】：")
        if quit_login == "1":
            exit_login()  # 跳转到退出用户函数
        elif quit_login == "2":
            print("返回成功")
    elif WHETHER_LOGIN["is_login"] == "error":
        ret = register_function()  # 调用注册函数
        print(ret)  # 将返回值输出


def login():  # 1用户登录
    print("用户登录".center(82, "="))
    username = input("请输入用户名：")
    passwd = input("请输入密码：")
    with open("user.txt", "r") as user:
        for line in user:
            f_user_list = line.strip("\n").split("|")  # 去除每行默认的回车，以及|，并且将它转换为列表赋给f_admin_list
            if f_user_list[0] == username and f_user_list[1] == passwd:
                print("登录成功")
                global USER_LIST
                USER_LIST = f_user_list  # 将获取到的当前行放到用户信息列表中
                WHETHER_LOGIN["is_login"] = "success"  # 登录成功将is_login的值设置success
                WHETHER_LOGIN["is_user"] = username  # 将我们登录的用户放入字典用，方便后期查询
                # print(USER_LIST)
                return f_user_list
        else:
            print("登录失败")


def main():
    while True:
        global COUNT
        COUNT += 1
        print("用户管理系统".center(80, "*") + "\n")
        print("1、用户登录；2：用户注册；3：修改密码；4：用户信息；5：用户管理；6：退出登录；7：退出程序")
        inp = input("请输入序号：")
        if inp == "1":
            if USER_LIST:
                if USER_LIST[3] == "1":
                    print("当前为管理员用户：【%s】，不能继续登录" % USER_LIST[0])
                else:
                    print("当前用户为【%s】,不能继续登录" % USER_LIST[0])
            else:
                login()
        elif inp == "2":
            register()
        elif inp == "3":
            alter()
        elif inp == "4":
            see()
        elif inp == "5":
            manage()
        elif inp == "6":
            exit_login()
        elif inp == "7":
            exit("程序已退出！！！")
        else:
            if COUNT == 3:
                exit("输入错误次数过多，程序自动退出。。。")
            else:
                print("输入有误，请重新输入。。。\n")
                continue


main()
