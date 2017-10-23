#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class http:
    def __init__(self, Host, Referer):
        self.header = {
                        # 'Content-type': 'application/x-www-form-urlencoded',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Host': Host,
                       'Referer': Referer,
                       # 'Pragma': 'no - cache',
                       # 'Cache - Control': 'no - cache',
                       # 'Accept - Encoding': 'gzip, deflate, br',
                       # 'Accept - Language': 'zh - CN, zh;q = 0.8',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                       }

    def request(self, method, **kwargs):
        conn = httplib.HTTPConnection(kwargs['host'])

        header = self.header.copy()
        if 'header' in kwargs:
            header.update(kwargs['header'])

        if 'data' not in kwargs:
            conn.request(method=method, url=kwargs['path'], headers=header)
        else:
            conn.request(method=method, url=kwargs['path'], body=urllib.urlencode(kwargs['data']), headers=header)

        res = conn.getresponse()
        return res
