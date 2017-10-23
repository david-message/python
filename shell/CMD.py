#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import commands
import time
import progressbar

reload(sys)
sys.setdefaultencoding('utf8')

def cmd():
    print commands.getoutput('ls -al')

    if __name__ == '__main__':
        for i in range(1, 61):
            sys.stdout.write('#' + '->' + "\b\b")
            sys.stdout.flush()
            time.sleep(0.5)
    print

def processer():
    total = 1000
    progress = progressbar.ProgressBar()
    for i in progress(range(total)):
        time.sleep(0.01)

    pbar = progressbar.ProgressBar().start()
    for i in range(1, 1000):
        pbar.update(int((i / (total - 1)) * 100))
        time.sleep(0.01)
    pbar.finish()

    # 高级用法
    widgets = ['Progress: ', progressbar.Percentage(), ' ', progressbar.Bar(marker=progressbar.RotatingMarker('>-=')),
               ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10 * i + 1)
        time.sleep(0.0001)
    pbar.finish()

if __name__ == '__main__':
    # cmd()
    processer()