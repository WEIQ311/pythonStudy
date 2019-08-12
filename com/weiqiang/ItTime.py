# -*- coding: UTF-8 -*-
# 导入正则匹配包
# 导入urllib模块
import re
import urllib

import ItTimeContent as it


# 步骤
# 1.确定要爬取数据的网址
# 2.获取该网址的源码
# 3.使用正则表达式去匹配网址的源码（匹配所需要的数据类型）
# 4.将爬取的数据保存至本地或者数据库

# 爬取网站页数、url前缀、多页分割符、后缀
def itTimeInfo(pageSize, urlPrefix, urlSplitter, urlSuffix):
    titles, contents, images, brieies, authors, itItems = [], [], [], [], [], []
    for item in range(pageSize):
        # 确定要爬取数据的网址
        if item == 1:
            url = urlPrefix + urlSuffix
        else:
            url = urlPrefix + urlSplitter + bytes(item) + urlSuffix
        # url = "https://www.ittime.com.cn/news/zixun.shtml"
        # 该网址的源码(以该网页的原编码方式进行编码，特殊字符编译不能编码就设置ignore)
        webSourceCode = urllib.urlopen(url).read().decode("utf-8", "ignore")
        # 匹配数据的正则表达式
        # 所有的图片
        imgRe = re.compile(r'src="(.*?\.jpg)" class="listimg"')
        # 所有的标题
        titleRe = re.compile(r'<h2><a href=".*?" target="_blank">(.*?)</a></h2>')
        # 正文
        contentRe = re.compile(r'<h2><a href="(.*?)" target="_blank">.*?</a></h2>')
        # 所有的简介
        briefRe = re.compile(r'<p>(.*?)</p>')
        # 所有的作者
        authorRe = re.compile(r'<span class="pull-left from_ori">(.*?)<span class="year">(.*?)</span></span>')
        # 匹配网页对应的标题数据
        titles.extend(titleRe.findall(webSourceCode))
        contents.extend(contentRe.findall(webSourceCode))
        images.extend(imgRe.findall(webSourceCode))
        brieies.extend(briefRe.findall(webSourceCode))
        authors.extend(authorRe.findall(webSourceCode))
    if len(titles) == len(images) == len(brieies) == len(authors):
        for item in range(len(titles)):
            pass
            # print titles[item], 'https://www.ittime.com.cn' +images[item], content[item], authors[item][0], authors[item][1]
            titleUrl = 'https://www.ittime.com.cn' + contents[item]
            itTime = ItTime(titles[item], it.contentInfo(titleUrl),
                            'https://www.ittime.com.cn' + images[item], brieies[item], authors[item][0],
                            authors[item][1])
            itItems.append(itTime)

    return itItems


# 定义对象
class ItTime:
    # 标题、正文、图标、简介、作者、发布时间
    title, content, image, brief, author, time = '', '', '', '', '', ''

    # 初始化
    def __init__(self, title, content, image, brief, author, time):
        self.title = title
        self.content = content
        self.image = image
        self.brief = brief
        self.author = author
        self.time = time

    # toString
    def info(self):
        return 'title:' + self.title + '\tcontent:' + self.content + ',\timage:' + self.image + ',\tbrief:' + self.brief + ',\tauthor:' + self.author + ',\ttime:' + self.time


# 判断变量类型的函数
def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "list"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    return type


if __name__ == '__main__':
    pageSize = 3
    urlPrefix = 'https://www.ittime.com.cn/news/zixun'
    urlSplitter = '_'
    urlSuffix = '.shtml'
    itTimes = itTimeInfo(pageSize, urlPrefix, urlSplitter, urlSuffix)

    for itItem in itTimes:
        # print itItem.title
        print itItem.info()
