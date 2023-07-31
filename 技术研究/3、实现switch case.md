引用：https://mp.weixin.qq.com/s/9KukXCwHXVefM_N9q8y70Q
注意：3.9不支持

Python如何实现switch case？

想学Python高级编程？必须了解这个小技巧！YYDS

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/%E9%AB%98%E7%BA%A7%E7%BC%96%E7%A8%8B/2%E3%80%81match-case/cover.png)

大家好，这里是程序员晚枫，小破站/知乎/小红书/抖音都叫这个名字。

上次给大家分享了[Python高级编程第一讲：从使用类型提示开始](https://mp.weixin.qq.com/s/mmRunGwi09QyGBxCL2aq2A)
；今天分享Python高级编程**第二讲：深入解析Python中switch case的使用方法**。

## 1\写在前面

分享之前，先说几点注意事项：

- Python对switch case的支持，来自PEP634，如下图所示。
- Python对switch case的支持，是通过match case实现的。语法稍有不同，作用完全一致。
- 经过测试，Python对switch case的支持是从3.10开始的，网上有部分文章说是3.11才开始支持是错误的。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/%E9%AB%98%E7%BA%A7%E7%BC%96%E7%A8%8B/2%E3%80%81match-case/pep634.png)

## 代码演示

如下代码所示，在没有match case之前，我们通常是通过if else做匹配的。

然而，随着编程语言的不断发展，现在很多语言都已经提供了更加方便和高效的匹配方式，例如Swift语言中的switch语句。switch语句不仅可以匹配基本数据类型，还可以匹配枚举类型、元组等更加复杂的数据结构。

**而且，使用switch语句的可读性和可维护性也更好，代码量更少。**

因此，如果你使用的编程语言支持switch语句，建议在匹配时优先考虑使用它。当然，在某些情况下，if else也可以更好地解决问题，关键是根据具体情况选择最合适的匹配方式。

总之，无论是if else还是switch，都需要掌握它们的使用方法，以便在实际编程中灵活运用。

```python

def select_platform(name):
    if name == "小破站":
        print(f"程序员晚枫的{name}主页链接是：https://space.bilibili.com/1989702333")
    elif name == "Z乎":
        print(f"程序员晚枫的{name}主页链接是：https://www.zhihu.com/people/CoderWanFeng")
    elif name == "小红薯":
        print(
            f"程序员晚枫的{name}主页链接是：https://www.xiaohongshu.com/user/profile/611dcb820000000001014aca?xhsshare=CopyLink&appuid=611dcb820000000001014aca&apptime=1690386848")
    else:
        print(f"程序员晚枫的默认主页链接是：https://www.python-office.com/")


select_platform("小破站")
# Output: 程序员晚枫的小破站主页链接是：https://space.bilibili.com/1989702333
select_platform("Z乎")
```

有了match case之后，我们可以这样做匹配：

```python

def select_platform(name):
    match name:
        case "小破站":
            print(f"程序员晚枫的{name}主页链接是：https://space.bilibili.com/1989702333")
        case "Z乎":
            print(f"程序员晚枫的{name}主页链接是：https://www.zhihu.com/people/CoderWanFeng")
        case "小红薯":
            print(
                f"程序员晚枫的{name}主页链接是：https://www.xiaohongshu.com/user/profile/611dcb820000000001014aca?xhsshare=CopyLink&appuid=611dcb820000000001014aca&apptime=1690386848")
        case _:
            print(f"程序员晚枫的默认主页链接是：https://www.python-office.com/")


select_platform("小破站")
# Output: 程序员晚枫的小破站主页链接是：https://space.bilibili.com/1989702333
select_platform("Z乎")
# Output: 程序员晚枫的Z乎主页链接是：https://www.zhihu.com/people/CoderWanFeng

```

## 写在最后

这个新特性的效率怎么样呢？我查询了网上众多大佬的测评，初步结论是：很遗憾，它的效率低于if-else。

然而，我们不能完全否定这个新特性的价值。虽然相对于if-else，它的效率略低，但是在某些情况下，它可以提高代码的可读性和简洁性，从而减少错误和提高开发效率。此外，这个新特性还可以有效地避免一些常见的编程错误。

**因此，我们需要在实际开发中综合考虑各种因素，选择最适合自己项目的编程风格和技术方案，以达到更好的开发效果和用户体验。**

你会把这个新特性用在自己的项目里吗？在评论区写下你的答案吧~
