#!/usr/bin/env python
# encoding: utf-8

import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(args)
        end = time.clock()
        print 'used:', end - start
    return wrapper

class Tester(object):
    def __init__(self):
        pass

    @timeit
    def method_01(self):
        print 'in foo()'

if __name__ == "__main__":
    Tester().method_01()








