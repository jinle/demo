#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import math
from operator import methodcaller


def simp_func(a, b):
    print("simp_func: a={0} b={1}".format(a, b))


class A():

    def obj_func(self, a, b):
        print("obj_func: a={0} b={1}".format(a, b))


if __name__ == '__main__':

    # 调用本模块的方法
    func1 = getattr(sys.modules[__name__], "simp_func")
    func1(2, 3)

    # 调用系统自带模块的方法
    func2 = getattr(math, "sqrt")
    print("sqrt({0}) = {1}".format(5, func2(5)))

    # 调用类对象的方法
    a = A()
    methodcaller("obj_func", 5, 6)(a)
