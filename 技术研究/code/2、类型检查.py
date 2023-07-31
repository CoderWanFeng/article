# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/28 1:29 
@本段代码的视频说明     ：
'''
name: str = '程序员晚枫'
fans: int = 24

def info(name: str, fans: str) -> str:
    return f'我的小破站是：{name}，粉丝数是：{fans}'


dict_of_users: dict[int, str | int] = {
    '小破站': "程序员晚枫",
    '小红薯': "程序员晚枫",
    '某乎': 1
}


class Account:
    def __init__(self, name: str, fans: int):
        self.name = name
        self.fans = fans


def info(account: Account) -> str:
    return f'我的小破站是：{account.name}，粉丝数是：{account.fans}'
