#!/usr/bin/env python
# -*- coding:utf-8 -*-
from queue import Queue
from threading import Thread
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        #time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    c = 0
    while True:
        value = q.get()
        print('Get %s from queue.' % value)
        time.sleep(random.random())
        c += 1
        if c == 3:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Thread(target=write, args=(q,))
    pr = Thread(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('所有数据都写入并且读完')