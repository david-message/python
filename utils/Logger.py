# /usr/bin/python
# -*- coding: utf-8 -*-

import ConsoleColor


def err(*msg):
    newMsg = filter(msg)
    for m in newMsg:
        print ConsoleColor.UseStyle(m, fore='red', mode='blink'),
    print ''


def warn(*msg):
    newMsg = filter(msg)
    for m in newMsg:
        print ConsoleColor.UseStyle(m, fore='yellow'),
    print ''


def info(*msg):
    newMsg = filter(msg)
    for m in newMsg:
        print ConsoleColor.UseStyle(m, fore='blue'),
    print ''


def filter(arr):
    # newArr = []
    # for i in range(0, len(arr)):
    #     newArr.append(arr[i].encode("UTF-8"))
    # return newArr
    return arr
