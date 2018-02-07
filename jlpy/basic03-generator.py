#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong

# 问题的提出：
# 1） 创建一个巨大的列表而仅仅需要访问其中少量几个元素。
# 2） 如果列表元素可以安装某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#     这样就不必创建完整的list，从而节省大量的空间。

# 生成器，迭代器，可迭代对象的区别？？？

# 生成生成器：列表推导时用()替换[]。

print(type(range(10)))

# 平方表
square_table = []
for i in range(50000):
    square_table.append(i * i)
for i in range(10):
    print(square_table[i])

# 用生成器, 把真正的计算推迟到你使用的时候，用时再算。
# 必须从头儿开始迭代，不能从中间开始。元素可以做到实时生成。
square_generator = ( x * x for x in range(50000))
print(type(square_generator))
for i in range(10):
    print(next(square_generator))

# for i in range(10):
#     print(next(square_generator))

def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

import traceback
f = fib(5)  # 限定到5个
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
    print(next(f))
except StopIteration:
    #print("stop iteration")
    traceback.print_exc()
for i in fib(5):
    print(i)