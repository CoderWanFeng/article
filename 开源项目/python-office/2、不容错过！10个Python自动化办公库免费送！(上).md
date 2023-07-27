# 全部免费！整理了10个Python自动化办公库！(上)


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/python-office%2F10%E4%B8%AA%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC%E5%BA%93%2Fcover.jpg)

大家好，这里是程序员晚枫，B站也叫这个名。

今天给大家分享一下，花费2周时间整理的Python自动化办公库。

本次内容涵盖了Excel、Word、PPT、PDF、微信、文件处理等所有能在办公场景实现自动化的库，希望能够对大家有所帮助。

> 提前说一下，以下所有仓库和代码，都是在网络上开源免费的！这次先分享5个，后面会继续分享剩下的5个，点关注不迷路哟~
## 1、Excel自动化库：poexcel
### 官网

``https://pypi.org/project/poexcel/``

### 功能举例
- 自动创建
- 合并
- 搜索Excel文件
- Excel转PDF
- 等
### 代码举例

```python
import poexcel

poexcel.fake2excel(columns=['name', 'text'], rows=20)
```


## 2、Word自动化库：poword
### 官网

``https://pypi.org/project/poword/``

### 功能举例
- Word转PDF
- 合并Word
- doc和docx互转
- 等
### 代码举例

```python
import poword

poword.docx2pdf(path=r'd://程序员晚枫的Word.docx', output_path=r'e://晚枫的文档.pdf')
```


## 3、PPT自动化库：poppt
### 官网

``https://pypi.org/project/poppt/``

### 功能举例
- PPT转为一张长图
- 合并PPT
- 等
### 代码举例

```python
import poppt

input_path = r"D:\小破站\程序员晚枫\github\poppt\dev\docs"
poppt.merge4ppt(input_path)
```

## 4、PDF自动化库：popdf
### 官网

``https://pypi.org/project/popdf/``

### 功能举例
- PDF转为Word
- 从PDF里提取表格
- 加水印
- PPT转PDF
- 等
### 代码举例

```python
import popdf

file_path = r'e://晚枫的文档.pdf'
output_path = r'd://程序员晚枫的Word.docx'

popdf.pdf2docx(file_path, output_path)
```

## 5、文件自动化库：pofile、search4file
### 官网

``https://pypi.org/project/pofile/``

``https://pypi.org/project/search4file/``


### 功能举例
- 批量重命名
- 根据内容，查找文件位置
- 自动整理文件夹
- 等
### 代码举例

```python
import search4file

# 1行代码，实现 
search4file.search_by_content(r'你的文件夹，例如：d:\\程序员晚枫的文件夹' , content="你需要查找的文件里面的内容，例如：所有平台都叫-程序员晚枫")
```

---

在使用中有问题，或者觉得本文有帮助，请在评论区告诉我吧~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/python-office/10%E4%B8%AA%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC%E5%BA%93/in-1.jpg)

