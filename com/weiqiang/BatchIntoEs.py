# -*- coding: UTF-8 -*-

import datetime
import time

from elasticsearch import Elasticsearch
from elasticsearch import helpers

import ItTime as it


# 数据入es
def itTime():
    pageSize = 10
    urlPrefix = 'https://www.ittime.com.cn/news/zixun'
    urlSplitter = '_'
    urlSuffix = '.shtml'
    itTimes = it.itTimeInfo(pageSize, urlPrefix, urlSplitter, urlSuffix)
    es = Elasticsearch("127.0.0.1")
    actions = []
    j = 0
    base = datetime.datetime.today()
    for itItem in itTimes:
        d1 = base - datetime.timedelta(days=j)
        ts = int(time.mktime(d1.timetuple()) * 1000)
        action = {
            "_index": "ittime",
            "_type": "ittime",
            "_id": j,
            "_source": {
                "title": itItem.title,
                "content": itItem.content,
                "image": itItem.image,
                "brief": itItem.brief,
                "author": itItem.author,
                "time": itItem.time,
                "timestamp": ts
            }
        }
        actions.append(action)
        j += 1
    helpers.bulk(es, actions)


if __name__ == '__main__':
    itTime()
    print('work done!')
