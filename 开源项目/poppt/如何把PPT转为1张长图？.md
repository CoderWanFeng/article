# 用Python白嫖WPS付费功能：PPT转为 1张 长图，1行代码搞定

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poppt/ppt2img-2/cover.jpg?q-sign-algorithm=sha1&q-ak=AKIDj3OAEuyi6x-Gg64IGfJSWmxsvglSwKk0Ez6-gv6l-R2HPf0hQgw0gu39-3roe7dV&q-sign-time=1686409748;1686413348&q-key-time=1686409748;1686413348&q-header-list=host&q-url-param-list=ci-process&q-signature=6567dba705aac061cb64584207134c2aaac520c3&x-cos-security-token=4pSLRb2s43lVKR15k7OU5j1SaTqr84qa87505965ca9391c1c017a0089371698bxTxnmYsxGbL2omBWefqpxKb5CB8HbIYRc7x071qoRSBdE5QgBJFr6RbiPIPX93aFLoer-Z1yp4Ijt2_JCsQbPGq-UMKWOFuOMEyx3QBVjEb5E64N4C0jtscIBjYqUqKAvPbZ0Bh8joFRE-58E3-Jea9Vew2xizTzbZYf0iG00aVqm-_IC-UqSdWbiZArdShV&ci-process=originImage)


大家好，这里是程序员晚枫，小红薯也叫这个名。读者群👉[点我直达](https://mp.weixin.qq.com/s/CadAaJUTUlXmTxJAjFUfPQ)。

上次在同名小破站给大家分享👉[1行代码，PPT转图片](https://mp.weixin.qq.com/s/KtxI8H0RVJEnYtB18T6XiQ)后，评论区有朋友反映：上次分享的是把50页PPT转成了50张图片，但他还想要把``1份PPT转成1张长图``的代码。

每一个读者的认真评论，都必须给安排~

今天我们就来一起看一下：如何把PPT转为1张长图片，只需要1行Python代码！


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poppt/ppt2img-2/to1img.jpg?q-sign-algorithm=sha1&q-ak=AKID0SadTZ_7P3fg4F-1Q6bpDqL1ypVKPSCYklPtlBLHgQuuugQsEpsmvtZYAVUlDMa5&q-sign-time=1686408657;1686412257&q-key-time=1686408657;1686412257&q-header-list=host&q-url-param-list=ci-process&q-signature=7e992916d3728213df5083abd0cee791a79a64b8&x-cos-security-token=4pSLRb2s43lVKR15k7OU5j1SaTqr84qa46ea21b577c789a51b18d5ec4c9fcfc5xTxnmYsxGbL2omBWefqpxAiehXAVfZ_YJEqVdULZsGKoHFUaq45gm2maX5LngABv3XOvmLUJW7UpoYfp800aaDbTXwF0Gn6S5Mvqjuso5_Y4YkNKsCJQ60yeLU-PnyVigwyIF9OTwHOH56kBvb9qWDWjJ420oxEtFpZrX40m8vIALAC0jV09fafQZXMr90fm&ci-process=originImage)

## 1、先上代码

PPT转图片功能，来自开源项目：``python-office``，下载命令：

```python
pip install python-office
```
实现功能的代码如下。👇
```
#pip install python-office
import office

office.ppt.ppt2img(input_path=r'D:\code\github\poppt\程序员晚枫\我的介绍.pptx',
                   output_path=r'./ppt2img',
                   merge=True)

"""
PPT转图片
Args:
    input_path: 存放PPT的位置，
                转换单个文件 → 可以写文件的路径
                转换单个文件 → 写文件夹的路径
    output_path: 结果图片的存储位置，可以不写，默认代码目录
    merge: True → 转为1张图片
        False → PPT有多少张，就转为多少张图片

Returns: None

"""
```


## 2、如何使用？

于是就有了下面这个快速的代码，帮助你在瞬息万变的股市里，快速做出买卖的决定！
本次分享的第三方库是：``pofinance``，一个开源的Python金融库。

> ⭐Python自动化办公，开源项目的地址：https://github.com/CoderWanFeng/python-office


如果 功能对你有帮助 或者 使用中有任何问题，请在评论区告诉我吧~

---





