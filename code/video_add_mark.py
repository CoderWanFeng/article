# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/13 20:46 
@本段代码的视频说明     ： https://blog.csdn.net/kd_2015/article/details/80157713
'''
# from moviepy.editor import *
#
# clip = VideoFileClip("D:\迅雷下载\8月13日\8月13日.mp4", audio=True)
# width, height = clip.size
# text = TextClip("vx:CoderWanFeng", font='Arial', color='white', fontsize=28)  # 水印内容
# set_color = text.on_color(size=(clip.w + text.w, text.h - 10), color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.6)
# set_textPos = set_color.set_pos(
#     lambda pos: (max(width / 30, int(width - 0.5 * width * pos)), max(5 * height / 6, int(100 * pos))))
# Output = CompositeVideoClip([clip, set_textPos])
# Output.duration = clip.duration
# Output.write_videofile("output.mp4", fps=30, codec='libx264')


import poimage

poimage.add_watermark(file=r'D:\download\50-02-PyCharm的安装.png', mark='B站：程序员晚枫', output_path=r'mark_img')
# office.image.add_watermark(file=r'C:\Users\Lenovo\Desktop\temp\pep634.png', mark='小红薯：程序员晚枫')

# for r,d,f in os.walk(r'D:\workplace\code\github\python-office\tests\test_files\excel\merge2sheet'):
#     print(r)


import povideo

povideo.mark2video(video_path=r'D:\迅雷下载\8月22日\8月22日.mp4')
import os
IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
# IMAGEMAGICK_BINARY = os.getenv('Path', 'auto-detect')
print(IMAGEMAGICK_BINARY)
