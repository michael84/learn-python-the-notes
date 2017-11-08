#!/usr/bin/env python
# *-*coding:utf-8*-*
# Author: Wei Tong

from jlpy_utils import title


### 1. 变量和类型

## 基本变量类型：整数，浮点数，字符串，布尔值，空值，函数，模块，类型，自定义类型

# 变量必须被定义：
try:
    # x =100  # 变量需要先定义。
    print(x)
except NameError:
    print('NameError: "x" is not defined' + '\n')

# 字符串：string
title("字符串：string")
print(type(1234))
print(type(123.45))
print(type(123.))
print(type('abc'))

# 容器：列表和元组
title("列表和元组的类型:")
print(type([1, 3, 4, 5, 'a', 'b']))
print(type((1, 'abc')))
print(type(set(['a', 'b', 3]))) # 集合
print(type({'a': 1}))

# 函数的类型
title("函数的类型:")
def func(a, b, c):
    print(a, b, c)
print(type(func))
a = func # 函数赋给一个变量，也可以求得类型
print(type(a))

# 模块的类型
title("模块的类型:")
import string
print(type(string))

# 类
title("类的类型:")
class MyClass():
    pass

print(type(MyClass))
myclass = MyClass()
print(type(myclass))

print("python中所有对象都是一个类，类本身也是一个类。")

# 堆： 一块公共的内存空间，谁分配谁回收。生命周期是全局的，不会自动清理。
#      所有的变量都是存放在堆上的，如x = 100, x指向存放100的内存地址。
# 栈： 所有在栈里的东西在函数调用结束后都会被清理掉。


### 2. 常见字符串处理 (!!!!!!!)

## 字符串不能被修改??!!

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
title("去除空格:")
s = '     abcd efg  '
print(s.strip()) # 返回的是一个新的字符串
print(s.lstrip())
print(s.rstrip())
print(s)

# 字符串的连接
title("字符串的连接:")
s1 = 'abc'
s2 = 'def'
print(s1 + s2)
print(s1 + '\n' + s2)

# 大小写
title("大小写:")
s = 'abc def'
print(s.upper())
print(s.lower())
print(s.upper().lower())
print(s.capitalize())

# 位置比较
title("位置比较:")
s_1 = 'abcdefg'
s_2 = 'abdeffefge'
print(s_1.index('bcd'))
try:
    print(s_2.index('bcd'))
except ValueError:
    pass
# 在Python3中，cmp函数被移除了。直接用大于，小于，等于去比较。
print(s_1 == s_2)
print(s_1 < s_2)
print(s_1 > s_2)

# 长度
title("长度:")
print(len('abcdefeagege'))
print(len(''))

s = ''
if not s: # 不能直接将字符串和布尔比较，用not
    print('Empty')

# 分割和连接
title("分割和连接")
s3 = 'abc,def,ghi'
splitted = s3.split(',')
print(type(splitted))
print(splitted)

s4 = """abc
def
ghijj
joifjwo"""
s_s1 = s4.split("\n")
s_s2 = s4.splitlines()
print(s_s1)
print(s_s2)

# 连接
s_j1 = ['abcd', 'ef123', 'weit']
print(','.join(s_j1))
print('-'.join(s_j1))
print('\n'.join(s_j1))

# 字符串的常用判断
title("分割和连接")
s_judge = 'vjjojgejoge'
print(s_judge.startswith('vjj'))
print(s_judge.endswith('oge'))

print('1234gegew'.isalpha())
print('1234gegew'.isalnum())
print('gegew'.isalpha())
print('1234324'.isdigit())
print('      '.isspace())
print('abc1343'.islower())
print('FWEFF'.isupper())
print('Hello world'.istitle())
print('Hello World'.istitle())

# 数字到字符串
title('数字到字符串')
print(str(5))   #数字转化为字符串
print(str(5.))
print(str(5.1234))
print(str(-5.123))

# 字符串到数字
title('字符串到数字')
print(int('1234'))
print(float('1234.56')) # 必须传正确的数字类型进去。

# 二进制，八进制，十进制，十六进制转换
title('二进制，八进制，十进制，十六进制转换')
print(int('11111', 2))
print(int('ffff', 16))

# 字符串到列表（数组）
title('字符串到列表（数组）')
s_l = 'baafegwg'
l = list(s_l)
print(l)


### 3. 条件判断

# if判断
title('if判断')
a = 100
b = 200
c = 300
if c == a:
    print(a)
elif c == b:
    print(b)
else:
    print(c)

# None的判断
title('None的判断')
x = None
if x is None: # is看起来更加直接。if not x:
    print('None')
elif not x:
    print('Not None 1')
else:
    print('not None')


### 4. 循环控制

# for循环
title('for循环')
for i in range(0, 30, 5): #可迭代的. python3中没有xrange了，只有range.
    print(i)

# while循环
title('while循环')
su = 0
i = 1
while i <= 100:
    su += i
    i += 1
print(su)

# continue&break
title('continue break')
for i in range(0, 100):
    if i < 10:
        pass
    elif i < 30:
        continue
    elif i < 35:
        print(i)
    else:
        break


### 5. 函数
title('函数')
def func_name(arg1, arg2):
    print(arg1, arg2)
    return arg1, arg2 #多个return实际上返回一个元组，只读的。
r = func_name(1, 2)
print(type(r))
print(r[0], r[1])
print(r)

# 函数：默认值参数
title('函数：默认值参数')
def func(x, y=500):
    return x + y
print(func(100, 600))
print(func(100))

print('参数位置调换：') # 不用严格按照顺序

def func1(x, y=500):
    print('x =', x)
    print('y =', y)
    return x + y

print(func1(100))
print(func1(y = 300, x = 200))
print(func1(x = 400))

# 函数： 可变参数
