# -*- coding: UTF-8 -*-
'''
@作者  ：小破站/抖音/微博/小红薯/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/26 23:57 
@本段代码的视频说明     ：
'''


def select_platform(name):
    if name == "小破站":
        print(f"程序员晚枫的{name}主页链接是：https://space.bilibili.com/1989702333")
    elif name == "Z乎":
        print(f"程序员晚枫的{name}主页链接是：https://www.zhihu.com/people/CoderWanFeng")
    elif name == "小红薯":
        print(
            f"程序员晚枫的{name}主页链接是：https://www.xiaohongshu.com/user/profile/611dcb820000000001014aca?xhsshare=CopyLink&appuid=611dcb820000000001014aca&apptime=1690386848")
    else:
        print(f"程序员晚枫的默认主页链接是：https://www.python-office.com/")


select_platform("小破站")
# Output: 程序员晚枫的小破站主页链接是：https://space.bilibili.com/1989702333
select_platform("Z乎")


# Output: 程序员晚枫的Z乎主页链接是：https://www.zhihu.com/people/CoderWanFeng


def select_platform(name):
    match name:
        case "小破站":
            print(f"程序员晚枫的{name}主页链接是：https://space.bilibili.com/1989702333")
        case "Z乎":
            print(f"程序员晚枫的{name}主页链接是：https://www.zhihu.com/people/CoderWanFeng")
        case "小红薯":
            print(
                f"程序员晚枫的{name}主页链接是：https://www.xiaohongshu.com/user/profile/611dcb820000000001014aca?xhsshare=CopyLink&appuid=611dcb820000000001014aca&apptime=1690386848")
        case _:
            print(f"程序员晚枫的默认主页链接是：https://www.python-office.com/")


select_platform("小破站")
# Output: 程序员晚枫的小破站主页链接是：https://space.bilibili.com/1989702333
select_platform("Z乎")


# Output: 程序员晚枫的Z乎主页链接是：https://www.zhihu.com/people/CoderWanFeng


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(5, 10)
print(result)  # Output: 15

result = add_numbers("Hello", "World")  # Type check error
print(result)

# my_list = [1, 2, 3]
#
# iterate my_list:
# print(item)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

name: int
age: int

name = input("Your name?")
age = int(input("Your age?"))
