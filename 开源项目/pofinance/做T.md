# 【Python金融-001】如何快速计算股票的收益？1行代码，高效做T

大家好，这里是程序员晚枫，小红书也叫这个名。读者群👉[点我直达](https://mp.weixin.qq.com/s/NN2pX2bQPpczOeGF4ARNtw)。

如果中年妇女的归宿是广场舞，那么中年男人的归宿想必就是股票了，懂得都懂。

在买卖股票时，一个重要的操作技巧就是做T，然而每次做T时计算价差、手续费，着实头疼。

今天给大家分享一下，**如何通过Python实现高效做T，把握住每一次交易机会，降低持仓成本。**


## 1、先上代码

股票收益，简单说就是高抛低吸：5块钱买进100股，10块钱卖出100股，收益的计算方式为：股数100*价差（10-5）=收入500元。很好理解对吧？

但这其中还涉及到一些手续费（0~万分之5）、印花税（千分之一）、转让费等，而且有些股票价格的变化微乎其微，每次可能只波动1分钱。什么价格买的、什么价格卖的，赚了还是赔了，计算起来就很复杂。

```
# pip install pofinance
import pofinance

good = pofinance.t0(11.2, 11.4, 100)
print(good)

"""
计算做T的收益
参数:
    buy_price: 买入成本
    sale_price: 卖出价格
    num: 单笔数量
    w_rate: 手续费，默认万2.5
    min_rate: 单笔最低手续费，默认5元
    stamp_tax: 印花税，默认千1

返回结果: 做T后的收益金额
"""
```

## 2、如何使用？

于是就有了下面这个快速的代码，帮助你在瞬息万变的股市里，快速做出买卖的决定！
本次分享的第三方库是：``pofinance``，一个开源的Python金融库。

> ⭐源代码地址：https://pypi.org/project/pofinance/

上面的代码复制粘贴就可以使用，使用时，你只需根据自己的股票价格填写6个参数，从左到右参数的含义一次是：

- buy_price: 买入时的价格
- sale_price: 卖出时的价格
- num: 单笔数量
- w_rate: 手续费，可以不填，默认是万2.5
- min_rate: 单笔最低手续费，可以不填，默认5元
- stamp_tax: 印花税，可以不填，默认千1

举个例子，我自己在摸鱼的间隙就会通过做T的方式，买入卖出自己看好的股票，降低自己的持仓成本。因为我每天操作的股数、手续费、单笔最低手续费和印花税都是固定的，所以我只需要填写**前2个参数：买入和卖出的价格，**就可以快速得到我每次操作的收益。

尤其是在急涨急跌的时候，这行代码可帮大忙了！但还是要提醒一句：``（股市有风险，投资需谨慎）``。


---





