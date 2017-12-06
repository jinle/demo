#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function


class A():

    def __init__(self, a):
        self.a = a

    def out(self, msg):
        print(msg, "self.a =", self.a)


def wrap_method(obj):
    obj.oldfunc = obj.out

    def wrap(msg):
        print("wrap ...")
        obj.oldfunc(msg)

    obj.out = wrap


if __name__ == "__main__":
    a = A(5)
    a.out("old value")
    wrap_method(a)
    a.out("new value")
