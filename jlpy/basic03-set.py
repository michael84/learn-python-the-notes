#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong

from jlpy_utils import title, sub_title


title("set")
# set就是去重的，无序的。 直接把一个list或者tuple给set。
s_a = set([1, 2, 2, 3, 4, 5, 6])
s_b = set([4, 5, 6, 7, 8, 9])
print(s_a)
print(s_b)

# 判断元素是否存在
print(5 in s_a)
print(0 in s_b)

# 并集
print(s_a | s_b) # 或操作, 并集
print(s_a.union(s_b))

# 交集
print(s_a & s_b) # &
print(s_a.intersection(s_b))

# 差集 A - A并B
print(s_a - s_b)
print(s_a.difference(s_b))

# 对称差 （A | B） - (A & B)
print(s_a ^ s_b)
print(s_a.symmetric_difference(s_b))

#修改元素, set中顺序随机，无序的。
s_a.add('x')
s_a.update([4, 5, 60, 70])
print(s_a)

# 删除元素，直接删除值。
s_a.remove(70) # 必须指定值。没有索引，无法通过下标访问。
print(s_a)
#s_a.remove(100) # 不存在元素会报KeyError: 100

print(len(s_a))
for i in s_a:
    print(i)