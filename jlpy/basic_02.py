#!/usr/bin/env python
# *-*coding:utf-8*-*
# Author: Wei Tong

### 1. 变量和类型

## 基本变量类型：整数，浮点数，字符串，布尔值，空值，函数，模块，类型，自定义类型

# 变量必须被定义：
try:
    # x =100  # 变量需要先定义。
    print(x)
except NameError:
    print('NameError: "x" is not defined' + '\n')

# 字符串：string
print(' string类型: '.center(20, '='))
print(type(1234))
print(type(123.45))
print(type(123.))
print(type('abc'))

# 容器：列表和元组
print(' 列表和元组的类型:'.center(20, '='))
print(type([1, 3, 4, 5, 'a', 'b']))
print(type((1, 'abc')))
print(type(set(['a', 'b', 3]))) # 集合
print(type({'a': 1}))

# 函数的类型
print(' 函数的类型: '.center(20, '='))
def func(a, b, c):
    print(a, b, c)
print(type(func))
a = func # 函数赋给一个变量，也可以求的类型
print(type(a))

# 模块的类型
print(' 模块的类型: '.center(20, '='))
import string
print(type(string))

# 类
print(' 类的类型: '.center(20, '='))
class MyClass():
    pass

print(type(MyClass))
myclass = MyClass()
print(type(myclass))

print("python中所有对象都是一个类，类本身也是一个类。\n")

# 堆： 一块公共的内存空间，谁分配谁回收。生命周期是全局的，不会自动清理。
#      所有的变量都是存放在堆上的，如x = 100, x指向存放100的内存地址。
# 栈： 所有在栈里的东西在函数调用结束后都会被清理掉。


### 2. 常见字符串处理 (!!!!!!!)

## 去除空格及特殊符号：strip，lstrip，rstrip
## 复制字符串：str1 = str2
## 连接字符串：
    # str2 += str1
    # new_str = str2 + str1
## 查找字符串： posi = str1.index(str2)
## 比较字符串：cmp(str1, str2)
## 字符串长度：len(str)
## 大小写转换：
#   u_str = str.upper()
#   l_str = str.lower()

## 首字母大写：str.capitalize(); str.capword(str)
## 分割与合并字符串（重要）：split, splitlines, join
## 类型转换：int, float转换
## 格式化字符串

import string

# 去除空格
s = '     abcd efg  '
print(s.strip()) # 返回的是一个新的字符串
print(s.lstrip())
print(s.rstrip())
print(s)

# 字符串的连接
s1 = 'abc'
s2 = 'def'
print(s1 + s2)
print(s1 + '\n' + s2)

# 大小写
s = 'abc def'
print(s.upper())
print(s.lower())
print(s.upper().lower())
print(s.capitalize())

# 位置比较
s_1 = 'abcdefg'
s_2 = 'abdeffefge'
print(s_1.index('bcd'))
try:
    print(s_2.index('bcd'))
except ValueError:
    pass
# 在Python3中，cmp函数被移除了。直接比较。
print(s_1 == s_2)
print(s_1 < s_2)
print(s_1 > s_2)

# 长度
print(len('abcdefeagege'))
print(len(''))

### 3. 条件判断

### 4. 循环控制

### 5. 函数




