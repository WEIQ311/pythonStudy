# -*- coding: UTF-8 -*-
# 导入正则匹配包
# 导入urllib模块
import os
import re
import sys
import urllib


def contentInfo(url='https://www.ittime.com.cn/news/news_29185.shtml', saveFile=False):
    reload(sys)
    sys.setdefaultencoding('utf8')
    content = []
    contentInfo = '';
    # 该网址的源码(以该网页的原编码方式进行编码，特殊字符编译不能编码就设置ignore)
    webSourceCode = urllib.urlopen(url).read().decode("utf-8", "ignore")
    fileName = url[url.rfind('/') + 1:url.rfind('.')]
    # 所有的内容
    contentRe = re.compile(r'<p>(.*?)</p>')
    content.extend(contentRe.findall(webSourceCode))
    if saveFile:
        # 为文件名称位置
        path = '../../fileInfo/'
        mkdir(path)
        fileInfo = path + fileName + '.txt'
        # 删除以前已经存在的文件
        if os.path.exists(fileInfo):
            os.remove(fileInfo)
        f = open(fileInfo, 'wb')
    contentRe = re.compile('</?\w+[^>]*>')
    for item in content:
        # print item
        # 过滤掉html标签内容
        if not re.match(contentRe, item):
            contentInfo += item + '\r\n'
    if saveFile:
        f.write(contentInfo)
        f.flush()
        f.close()
    return contentInfo


'''
创建文件夹
'''


def mkdir(path):
    # 文件夹不存在,则建文件
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    contentInfo(saveFile=True)
