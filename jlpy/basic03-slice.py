#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong


# 切片: [start:end:steps] 开区间：>= start & < end
# 存取序列（列表，元组，字符串）的任意一部分
# 默认值，负数索引，负数步长

li = list(range(10))
print(li)

print(li[2:5]) # 开区间
print(li[:4])
print(li[5:])
print(li[0:10:3])
print(li[0:15:3]) # 越界不管，只按实际大小来做计算。

# 负值怎么处理？
print(li[5:-2]) # [5, 6, 7]
print(li[9:0:-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(li[9::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(li[::-2]) # [9, 7, 5, 3, 1]

# 切片生成一个新的对象。
print(li)  # 还是保持原样。

# 用切片快速反转。用负数索引做切片。
re_li = li[::-1]
print(re_li)
