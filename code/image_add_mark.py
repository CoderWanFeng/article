# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/6/30 22:06 
@Description     ：
'''

import poimage

poimage.add_watermark(file=r'D:\download\地产中介宣传推广简约公众号首图.jpg', mark='B站：程序员晚枫', output_path=r'mark_img',color='#000000',opacity=0.04,
                      space=55,size=30,)
# office.image.add_watermark(file=r'C:\Users\Lenovo\Desktop\temp\pep634.png', mark='小红薯：程序员晚枫')

# for r,d,f in os.walk(r'D:\workplace\code\github\python-office\tests\test_files\excel\merge2sheet'):
#     print(r)
