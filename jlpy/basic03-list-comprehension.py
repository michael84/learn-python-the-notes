#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong

# 列表推导
# 问题的提出： 1） 快速简单的生产一个列表； 2） 对原有的列表进行简单的转换。
# 一维列表推导。
# 二维列表推导以及注意事项

# 最简单情况。
li = []
for i in range(10):
    li.append(i)
print(li)

li = [0] * 10
print(li)

# 生成前十个偶数
li = [ i * 2 for i in range(10)]   # 列表表达式？
print(li)

# 二维列表
'''
li_2d = [[0] * 3] * 3 # 浅拷贝，只是生成了索引。
print(li_2d)
li_2d[0][0] = 100
print(li_2d)
'''

li_2d = [[0] * 3 for i in range(3)]
li_2d[0][0] = 100
print(li_2d)

# 字典和集合在python3中支持这种推导。
s = {x for x in range(10) if x % 2 == 0}
print(type(s))
print(s)

d = {x: x % 2 == 0 for x in range(10)}
print(type(d))
print(d)

