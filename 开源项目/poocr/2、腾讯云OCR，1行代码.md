【腾讯云+OCR】只需1行Python代码实现OCR功能，批量图片转文字，现在可以免费用！

大家好，这里是程序员晚枫，今天给大家分享一个基于腾讯云开发的OCR功能，只需要1行Python代码即可实现！

本文分为3部分：

- 首先，进行一种场景（功能）下的图片转文字场景的代码演示；
- 其次，介绍共有100多个识别功能，如何通过一个统一格式的代码调用；
- 最后，说明腾讯云+OCR的免费额度使用情况。

## 代码演示

腾讯云提供了丰富的OCR使用场景，例如我之前分享过的：身份证识别、银行卡识别、发票识别、车牌识别等等。

其中大家最感兴趣的发票识别，可以通过以下代码实现。👇

```python
# pip install poocr
import poocr

# 获取id和key的地址：https://cloud.tencent.com/document/product/598/37140
id = '获取方式?'
key = '获取方式?'

# 全部功能 的文档：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.VatInvoiceOCR(
    # 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url ，如果2个都填，则只用在线图片img_url
    img_path=r'D:\workplace\code\程序员晚枫\全网同名\发票照片.jpg',
    id=id, key=key)
print(result)  # 输出json格式的识别结果
```

## 所有功能

除了上面演示的发票识别，腾讯云还有100多个OCR的功能，它们的调用方法都是一致的。👇

```python
# 只需要替换最后一个单词，参数都是一样的。
# 所有功能对应的单词：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
result = poocr.ocr.IDCardOCR() # 身份证识别
result = poocr.ocr.VatInvoiceOCR() # 发票识别
result = poocr.ocr.BankCardOCR() # 银行卡识别
```


## 免费额度

腾讯云文字识别产品家族包括通用文字识别、通用卡证识别、票据单据识别、文本图像增强、智能结构化识别、智能扫码以及特定场景识别等服务，开通后即可享受1,000次/月的免费调用额度，以免费资源包的形式在每个月1号自动发放到您的腾讯云账号中，仅在当月有效。详情请参见文字识别 > 免费额度。

----

在使用中有问题，或者觉得本文有帮助，请在评论区告诉我吧~
