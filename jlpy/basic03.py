#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong

## Lesson：容器 （数组，一段连续的内存空间。）
## 容器：
##      list/tuple
##      dict
##      set
## 切片
## 列表推导
## 生成器
## 迭代器

from jlpy_utils import title, sub_title

title("List")

# 基本操作：创建，list添加元素（append, extend），list删除元素（del, pop）。
#         根据索引读写，判断容器是否为空，字符串转换，容器元素数量，遍历。

sub_title("list元素访问：")
# 元素访问
l01 = [1, 2, 3, '456', [1, 2, 3], {1: 'one', 2: 'two'}]
print(type(list))
print(type(l01))

print(l01[0])
print(l01[-1]) #
print(l01[-2])

# 查找元素位置
sub_title("查找元素内容的位置：")
print(l01.index('456'))
print(l01.index([1, 2, 3]))
#print(l01.index(-1))

# 添加元素
sub_title("添加元素：")
l_a = [1, 2, 3]
l_a.append(4)
l_a.append(5)
l_b = [6, 7, 8]
#l_a.append(l_b)  #---> 结果： [1, 2, 3, 4, 5, [6, 7, 8]]
l_a.extend(l_b)
print(l_a)

# 判断list是否为空
sub_title("判断list是否为空：")
l_02 = []  # 即使列表为空，也是一个list类。l_02 = None 代表l_02什么都不是，不在内存分配空间。
if not l_02:
    print('Empty')  # 空和None不是一回事儿。not XX和 XX is None不是一回事儿。
if l_02 is None:    # 身份？
    print('None')

if len(l_02) == 0:
    print('Empty')

# 删除元素
sub_title("删除元素:")
l_del = [1, 2, 'a', 'b', 'c', {'a': 1, 'b': 2}, (4, 5, 6), 'delete me']
del(l_del[-1]) # del(list[index])
print(l_del)

# 遍历
sub_title("遍历数组")
for i in l01:
    print(i)
for i in range(len(l01)):
    print(l01[i])

# tuple: 只读，没有append方法
title("元组tuple:")
t = (1, 2, 3, '456')
print(type(t))
# t[0] = 'a' # ----> fail
# t.append['a']  # ----> fail

# two_sum.py
sub_title("basic03-two_sum.py")

title("dict 字典")  # key/value的数据结构，无序的！一个key对应一个value。对应多个值，用数组。
# dict可以作为数组的元素。dict内部是哈希表。
d = {'a': 1, 'b': 2, 1: 'one', 2: 'two', 3: [1, 2, 3]}
print(type(d))
print(d)

# 访问元素
sub_title("访问元素:")
print(d['a'])
print(d[1])
print(d[3])

# 判断key是否存在，key在Python内部是做了索引的。根据key来索引，而不是value。
sub_title("判断元素是否存在")
print('c' in d)
print(2 in d)
print('two' in d)

print(d)
print(len(d))
del(d[3])  # del(dict[key])
print(d)
print(len(d))

sub_title("字典dict的遍历：")
print(d)
for key in d:
    print(d[key])
print('...')
for key, value in d.items():
    print(key, value)
keys = d.keys()
print(type(keys))
print(keys)