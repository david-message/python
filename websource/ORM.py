#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import redis


class RedisCli:
    def __init__(self, **cfg):
        self.redisCli = self.initConfig(**cfg)

    def initConfig(self, **cfg):
        print cfg['host'], cfg['port']
        pool = redis.ConnectionPool(**cfg)
        self.redisCli = redis.Redis(connection_pool=pool)
        # self.redisCli = redis.Redis(cfg['host'], cfg['port'])
        return self.redisCli


if __name__ == '__main__':
    rc = RedisCli(host='127.0.0.1', port=6379, password='xzw')
    print rc.redisCli.hset('map', 'test', 'abc')

    # slaStartTime = 1505205321000
    # expireTime = 1505207121000
    #
    # print  ( (expireTime - slaStartTime) /1000)/60,'分'
