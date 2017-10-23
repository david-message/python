#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ORM
import json


class RedisStore(ORM.RedisCli):
    def __init__(self, **cfg):
        self.cli = ORM.RedisCli(**cfg)

    def put(self, name, url):
        j = {}
        j['name'] = name
        j['url'] = url

        if str(url).startswith('index.php?'):
            self.insertQueue(url)
        else:
            self.cli.redisCli.hset('fileList', name, url)

        # 原始数据集合
        self.cli.redisCli.hset('dataSet', name, json.dumps(j))

    def insertQueue(self, url):
        self.cli.redisCli.lpush('uelQueue', url)

    def fetchQueue(self):
        #
        n = None
        try:
            n = self.cli.redisCli.brpop('uelQueue', timeout=30)
        except Exception:
            return None

        if n != None:
            self.cli.redisCli.set('curUrl', n[1])
            return n[1]

        return None

    def fileList(self):
        key = 'fileList'
        list = self.cli.redisCli.hgetall(key)
        return list
