#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong

# 迭代器：
# 问题的提出：
# 1） 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 2） 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator（表示一个惰性循环计算的序列）。
# !!!生成器一定是迭代器，生成器是惰性计算的。

# 集合数据类型如list，dict，str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

from collections import Iterable
from collections import Iterator

print(isinstance([1, 2, 3], Iterable)) # 是可迭代对象
print(isinstance([1, 2, 3], Iterator)) # 不是迭代器

print(isinstance({}, Iterable))
print(isinstance(123, Iterable))
print(isinstance('abc', Iterable))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g, Iterable)) # 是可迭代的，就可以用for循环
for i in g:
    print(i)

print("---fib---")

def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(type(f))
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

for i in f:
    print(i)