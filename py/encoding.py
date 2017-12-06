#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function

import sys
import codecs


def test_py2(name, encoding):
    with open(name, "rU") as f:
        for line in f:
            print(len(line), line)
        print(type(line))


def test_py2_by_codecs(name, encoding):
    from codecs import open
    with open(name, "rU") as f:
        f = codecs.getreader(encoding)(f)
        for line in f:
            if sys.stdout.encoding:
                print(len(line), line.encode(sys.stdout.encoding))
            else:
                import locale
                print(len(line), line.encode(locale.getpreferredencoding()))

        print(type(line))


def test_py2_utf8(name, encoding):
    from codecs import open
    with open(name, "rU") as f:
        f = codecs.getreader(encoding)(f)
        for line in f:
            if sys.stdout.encoding:
                print(len(line), line.encode(sys.stdout.encoding))
            else:
                print(len(line), line.encode("utf8"))
        print(type(line))


def test_py3(name, encoding):
    with open(name, "rt", encoding=encoding) as f:
        for line in f:
            print(len(line), line)


def test_str():
    print("this is text.")
    print("this line包括中文")


def test_unistr():
    print(u"this is text.")
    print(u"this line包括中文")


def main():
    os = ["linux", "windows", "osx"]
    encoding = ["utf8", "gb2312"]
    print("sys.stdout.encoding=", sys.stdout.encoding)
    print()

    filelist = ["{0}-{1}.txt".format(x, y) for x in os for y in encoding]
    for os, encoding in [(x, y) for x in os for y in encoding]:
        name = "encoding/{0}-{1}.txt".format(os, encoding)
        print(name, ":")
        print("name", sys.stdout.name)
        if sys.version < "3":
            if sys.argv[-1] == "--codecs":
                test_py2_by_codecs(name, encoding)
            elif sys.argv[-1] == "--utf8":
                test_py2_utf8(name, encoding)
            else:
                test_py2(name, encoding)
        else:
            test_py3(name, encoding)

    test_str()
    test_unistr()


if __name__ == "__main__":
    main()
