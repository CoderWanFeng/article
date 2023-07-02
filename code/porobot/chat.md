# 免费搭建一个有脾气的聊天机器人,1行Python代码就够了！

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/porobot/chat/cover.jpg)
大家好，这里是程序员晚枫。

之前给大家免费分享了[【8讲】用Python制作一个微信机器人，1行代码人人可用](https://mp.weixin.qq.com/s/9aspEHdCiAdXK17AvHlu9Q)，很多人还想要**免费的智能聊天功能**。

今天终于开发出来了，让我们一起看一下，如何用1行代码，实现智能聊天。

我测试了很多次，回复一直很稳定，赶紧去试一下，这个机器人的回复是有脾气的哟~

## 1、先上代码

本次机器人功能，来自第三方库：``porobot``，下载命令如下：

```python
pip install porobot
```

下载完成后，只需要1行命令就可以聊天啦~

```python
import porobot

print(porobot.normal.chat("你好，我是程序员晚枫"))
```
运行上面几行代码的结果，如下图所示。👇

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/porobot/chat/chat.png)
## 2、开源仓库

本次使用的第三方库来自开源项目：``python-office``，其下含有日常办公、学习、生活常用的数十个不同功能的仓库。例如：

- poword：一个处理word的自动化办公仓库。
- pohan：一个神奇的汉语编程库。
- poocr：一个通用型的文字识别库，可以识别发票、车牌、身份证等。
- pofinance：一个用来摸鱼炒股的工具包。
- poppt：一个免费操作ppt的库，例如：可以把ppt转化为一张图片。
- 全部功能的介绍，详见官网：www.python-office.com

## 3、参与开发

开源项目离不开大家的支持，尤其是离不开大家对代码的共同开发和维护。

如果你开发了新的功能代码或者发现了代码中存在的Bug，请通过issue或者pr的形式，直接提交到以下项目的代码仓库里：

- 💻GitHub：https://github.com/CoderWanFeng/python-office
- 国内用户，可以使用Gitee：https://gitee.com/CoderWanFeng/python-office/

----

对本文内容有任何疑问或者觉得本文有帮助，请在评论区告诉我吧~

