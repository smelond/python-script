#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# File_type:多级菜单，修改版
# Filename:Multilevel_menu.py
# Author:smelond

menu = {
    "成都": {
        "锦江区": ['春西路', '塔子山', '三圣花乡市场'],
        "青羊区": ['宽窄巷子', '杜甫草堂', '文殊院'],
        "金牛区": ['成都欢乐谷', '成都植物园', '永陵博物馆']
    },
    "深圳": {
        "福田区": ['香蜜湖', '深圳莲花山公园', '深圳园博园'],
        "罗湖区": ['梧桐山', '仙湖植物园', '东门步行街'],
        "南山区": ['世界之窗', '深圳欢乐谷', '青青世界']
    },
    "北京": {
        "东城区": ['故宫', '王府井', '南锣鼓巷'],
        "西城区": ['北京动物园', '国家大剧院', '北海公园'],
        "宣武区": ['法源寺', '古陶文明博物馆', '北京大观园']
    },
}
menu_list = list(menu.keys())#将字典转换为列表，但是这个只能转换key，而且是第一个key，比如成都

true_or_false = False#给他赋值为false
while true_or_false is not True:#如果true_or_false不为真时，执行接下来的语句
    print("城市信息表".center(50, "="))#打印提示
    print("q 或 quit 退出")#打印提示
    for index, key in enumerate(menu):#enumerate用来给他加上一个序号
        print(index, ":", key, end="\t\t")#index为打印的序号，key为打印的值
    city_input = input("\n请输入对应的序号：")#将输入的值赋给city_input
    if city_input.isdigit():#判断输入的是否为数字
        city_input = int(city_input)#如果为数字，将他转换为int型
        if city_input >= 0 and city_input <= len(menu_list):#判断输入的是否大于等于0并且小于我们key值得数量
            city_name = list(menu[menu_list[city_input]].keys())#这句我实在没看懂什么意思,百度到的，表示我的逻辑有问题
            # print(city_name)
            for index, key in enumerate(city_name):
                print(index, ":", key, end="\t\t")#还是循环输出，但是这回输出的是：锦江区那种类型的
            city_input_two = input("\n请输入对应的序号：")
            if city_input_two.isdigit():
                city_input_two = int(city_input_two)
                if city_input_two >= 0 and city_input_two <= len(city_name):
                    city_region = city_name[city_input_two]#下面有问题，目前学的知识，加我的逻辑能力，无法做出来

            else:
                if city_input_two == "q" or city_input_two == "quit":#退出比价拿手，每一级都能退出
                    exit("感谢你的使用")
    else:
        if city_input == "q" or city_input == "quit":
            exit("感谢你的使用")