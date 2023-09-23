# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/6/30 22:06
@Description     ：
'''

import poimage

# 一行代码，给图片加水印
poimage.add_watermark(file=r'D:\download\50-05-docx2pdf.png', mark='B站：程序员晚枫',
                      output_path=r'D:\workplace\code\gitee\python-office.com\docs-pages\vuepress\course\xmind\imgs')
