# 全部免费！整理了10个Python自动化办公库！(下)


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/python-office%2F10%E4%B8%AA%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC%E5%BA%93%2Fcover.jpg)

大家好，这里是程序员晚枫，B站也叫这个名。

今天给大家分享一下，花费2周时间整理的Python自动化办公库。

本次内容涵盖了Excel、Word、PPT、PDF、微信、文件处理等所有能在办公场景实现自动化的库，希望能够对大家有所帮助。

> 提前说一下，以下所有仓库和代码，都是在网络上开源免费的！
> 
> 上次已经给大家分享了5个：[全部免费！整理了10个Python自动化办公库！(上)](https://mp.weixin.qq.com/s/5KWHosZWE7SdM_qeEOpfXw)
> 
> 这次给大家分享剩下的5个，点关注不迷路哟~
## 1、聊天机器人自动化库：PyOfficeRobot
### 官网

``https://www.python-office.com/office/robot.html``

### 功能举例
- 
- 自动发消息
- 自动发文件
- 根据关键词回复
- 智能聊天
- 等
### 代码举例

```python
# 首先，将PyOfficeRobot模块导入到我们的代码块中。
# pip install PyOfficeRobot
import PyOfficeRobot

PyOfficeRobot.chat.send_message(who='小红书：程序员晚枫', message='你好')
```


## 2、图片自动化库：poimage
### 官网

``https://pypi.org/project/poimage/``

### 功能举例
- 图片加水印
- 免费生成动漫头像
- 解析二维码图片
- 等
### 代码举例

```python
# pip install poimage
import poimage

poimage.add_watermark(file=r'D:\抖快-程序员晚枫-头像.jpg', mark='程序员晚枫', output_path=r'./mark_img')
```


## 3、金融自动化库：pofinance
### 官网

``https://pypi.org/project/pofinance/``

### 功能举例
- 单次做T
- 批量做T
- 等
### 代码举例

```python
# pip install pofinance
from pofinance import MakeT

t = MakeT()
"""
加载手续费
Args:
    w_rate: 手续费，默认万2.5
    min_rate: 单笔最低手续费，默认5元
    stamp_tax: 印花税，默认千1
"""
sale_price_num = [(900, 12), (300, 11),(800, 10)]
res=t.batch_t(sale_price_num)
print(res)
```

## 4、视频自动化库：povideo
### 官网

``https://pypi.org/project/povideo/``

### 功能举例
- 视频转音频
- 视频提取字幕
- 等
### 代码举例

```python
# pip install povideo
import povideo

povideo.video2mp3(path=r'd://程序员晚枫的VLOG.mp4', mp3_name='result')
```

## 5、工具自动化库：wftools
### 官网

``https://pypi.org/project/wftools/``


### 功能举例
- 翻译万国语言
- 查询天气
- 解析IP地址
- 破解wifi密码
- 等
### 代码举例

```python
# pip install wftools
import wftools

wftools.weather()
```

---

在使用中有问题，或者觉得本文有帮助，请在评论区告诉我吧~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/python-office/10%E4%B8%AA%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC%E5%BA%93/in-1.jpg)

