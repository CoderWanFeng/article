基于Python的一个开源OCR工具，轻松实现批量图片转文字

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poocr/0.0.9-%E8%85%BE%E8%AE%AFocr%E6%B4%BB%E5%8A%A8/cover.jpg)

大家好，这里是程序员晚枫，小红薯也叫这个名。

之前的视频给大家分享了：[不容错过！10个Python自动化办公库免费送！](https://cloud.tencent.com/developer/article/2302410)

今天给大家分享一下，**基于Python的一个开源OCR工具，轻松实现批量图片转文字**

## 1、先说原理

本次分享的所有OCR功能，有100多种使用场景，例如：识别发票、识别身份证、识别银行卡等等。

识别准确率接近100%，所有功能的实现都是基于腾讯云提供的OCR接口。并且在官方接口的基础上，做了2次封装，从而仅用1行代码就可以调用所有功能。


- 所有功能的说明：[Python实现图片文字提取，准确率高达99%，100多个功能全给你！](https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg)

封装后的第三方库是：``poocr``，完全免费开源，下载和安装命令如下。👇

```
pip install poocr
```
## 2、演示代码
### 1、识别身份证
可以基于以下代码，做一个用户信息收集系统。

```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.IDCardOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\身份证照片，正反都行.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```
### 2、识别银行卡
```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.BankCardOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\银行卡照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```
### 3、识别发票
可以基于以下代码，做一个发票管理系统。
```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.VatInvoiceOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\发票照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```
### 4、识别车牌
可以基于以下代码，做一个停车场管理系统。

```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.LicensePlateOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\车牌照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```
### 5、识别二维码
可以基于以下代码，做一个二维码识别系统。

```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
id = '获取方式👆'
key = '获取方式👆'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.QrcodeOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\二维码照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```

---


如果以上代码对你有帮助，或者在使用过程中有任何问题，请在评论区和我交流~





