# 自动化办公更简单了！新版python-office，有哪些更新？

大家好，这里是程序员晚枫，小破站/小红薯都叫这个名。

去年4月开源了一个Python自动化办公项目：python-office，GitHub和Gitee都能看到。1行代码实现复杂的自动化办公任务，帮助不懂代码的小白，快速使用Python。

今年8月份开始，根据这个开源项目，在``小破站：Python自动化办公社区``更新了一套全新的课程：[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzI2Nzg5MjgyNg==&scene=1&album_id=3056320585091366915&count=3&uin=&key=&devicetype=Windows+11+x64&version=63090621&lang=zh_CN&ascene=0)。

在更新课程的同时，也在不断改进这个开源项目，包括：增加功能、修复Bug、优化速度等等。

目前课程已经更新到了第18讲，今天我们就来一起看一下，最新版python-office有哪些改进~


## 0、写在前面



项目源码地址在GitHub和Gitee都有：

- GitHub：https://github.com/CoderWanFeng/python-office
- Gitee：https://gitee.com/CoderWanFeng/python-office/



另外，在交流项目之前，建议你把本地的``python-office``免费升级到最新版，命令如下：👇

```python
pip install python-office -U
```
这段代码的作用：

- 如果你之前没下载过python-office，帮你自动下载并且安装最新版python-office，
- 如果你已经下载了python-office，帮你自动更新到最新版python-office。



## 1、适配了Mac和Linux的下载

以前python-office是不支持Mac和Linux系统下载的，现在支持下载了。

但是请注意，也仅仅是支持下载：在Mac和Linux系统上，运行``pip install python-office``的时候不会报错了，但是涉及到具体功能的使用，依然会报错。

距离真正适配所有功能的目标，万里长征才走了第一步。


## 2、完善docstring和功能说明

之前一直顾着开发新功能，忽略了注释的编写。这次使用Google的docstring风格完善了所有已录制功能的注释。如下图所示。👇

图片

## 3、增加功能演示的装饰器

小白刚拿到代码，不知道怎么用，这是新人常见问题。

没关系，这次更新通过增加``@instruction``装饰器,使每一个功能运行时，都会自动显示每个功能对应的演示视频，帮助小白更好的使用``python-office``。

例如运行一段**PDF转Word的代码**，你会看到下图显示。👇

图片

## 4、添加了Type Hints

众所周知，Python是一个弱类型语言，传参的时候不容易知道每个参数的类型。

这次为了更好的帮助专业人员使用``python-office``，特别增加了Type Hints。如下图所示。👇

图片


## 5、增加了pylint代码审查

灵活性是Python代码的优点，但是太灵活的编写代码，也导致Python代码写起来没有了规范。

这次为了让代码更符合规范，专门给自己增加了``pylint``这个代码审查工具，严格按照``PEP8``的标准编写代码。

每次提交之前都检查一次，也欢迎大家纠正错误。


## 6、官网也更新了

和开源项目更新一样重要的是官网：开源项目的文档，www.python-office.com  。

尝试过添加更多互动功能，最终因为服务器配置太低放弃了。

只在内容上做了改进，更加方便大家的阅读，大家可以打开看一下。

----

截止写这篇文章，[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzI2Nzg5MjgyNg==&scene=1&album_id=3056320585091366915&count=3&uin=&key=&devicetype=Windows+11+x64&version=63090621&lang=zh_CN&ascene=0)更新到第18讲了，接下来会加快更新速度，也欢迎大家加入读者交流群，对课程和项目中提出自己的创意或者代码~👇

图片

