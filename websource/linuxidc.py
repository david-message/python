#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import netUtil
from pyquery import PyQuery as pyq
import sys
import base64
import stroe
import traceback

reload(sys)
sys.setdefaultencoding('utf8')


def getHtml(path):
    config = {
        'host': 'linux.linuxidc.com',
        'Referer': 'http://linux.linuxidc.com/index.php?folder=MjAxMsTq18rBzw==',
    }

    # config = {
    #     'host': 'www.baidu.com',
    #     'Referer': 'http://www.baidu.com/',
    # }

    http = netUtil.http(
        Host=config['host'],
        Referer=config['Referer']
    )

    response = http.request(method='GET',
                            host=config['host'],
                            path='http://linux.linuxidc.com/' + path,
                            header={
                                'Accept': 'text/html, application/xhtml + xml, application/xml;q = 0.9, */*;q = 0.8',
                                # 'Accept-Encoding': 'gzip, deflate',
                                # 'Accept-Language': 'zh-CN, zh;q = 0.8',
                                'Cookie': 'Hm_lvt_05ff9e4b77acc9197fb1fe12f47d29fb=1505359552; Hm_lpvt_05ff9e4b77acc9197fb1fe12f47d29fb=1505359552; PHPSESSID=pah7g1q666v2d3u9kdvn9h84h5',
                                # 'Upgrade-Insecure-Requests': 1,
                                # 'Connection': 'keep-alive'
                            }
                            )

    # print(response.status)
    # print 'response.msg:'
    # print(response.msg)
    # print 'Cookie:'
    # print(response.getheader('Set-Cookie'))
    # print 'Content:'
    res = response.read().decode('gbk')
    # print res

    # debugHtml = open('../html/debug.html', 'w')
    # debugHtml.write(res)
    # debugHtml.close()
    print path
    return res


def parse(html):
    doc = pyq(html)
    # t=doc('body').find('table')
    t = doc('html').find('body').find('table')
    print t.length
    list = []
    if t.length >= 10:
        for a in t.eq(9).find('a'):
            href = pyq(a).attr('href')
            print a.text, href
            list.append({'name': a.text, 'url': href})
    return list


def doIt():
    rc = stroe.RedisStore(host='127.0.0.1', port=6379, password='xzw')

    while True:
        url = None
        try:
            url = rc.fetchQueue()
        except Exception, e:
            print 'str(Exception):\t', str(Exception)
            print 'str(e):\t\t', str(e)
            print 'repr(e):\t', repr(e)
            print 'e.message:\t', e.message
            print 'traceback.print_exc():';
            traceback.print_exc()
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            break

        if url == None:
            break

        html = getHtml(url)
        list = parse(html)
        for data in list:
            rc.put(data['name'], data['url'])


def initData():
    rc = stroe.RedisStore(host='127.0.0.1', port=6379, password='xzw')
    debugHtml = open('../html/debug.html', 'r+')
    list = parse(debugHtml.read())
    for data in list:
        rc.put(data['name'], data['url'])


def fileList():
    rc = stroe.RedisStore(host='127.0.0.1', port=6379, password='xzw')
    list = rc.fileList()
    for f in list:
        print f


if __name__ == '__main__':
# print base64.decodestring('MjAxMcTq18rBzw==').decode('gbk')
# initData()
# doIt()
    fileList()
