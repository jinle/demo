#!/usr/bin/env python
# -*- coding:utf-8 -*-


class WrapFile:

    def __init__(self, fobj):
        self.fobj = fobj
        self.line = None

    def put(self, line):
        self.line = line

    def __iter__(self):
        return self

    def __next__(self):

        if self.line is None:
            return self.fobj.__next__()
        else:
            x = self.line
            self.line = None
            return x


with open("e:/jinle/logdog/mytest.py", "rt") as f:
    mf = WrapFile(f)
    for no, line in enumerate(mf):
        if no == 2:
            mf.put("dddddd\n")
        print(no, line, end="")

