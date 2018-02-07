#!/usr/bin/env python
# *-*coding:utf-8*-*
# Author: Wei Tong

from jlpy_utils import title

### 1. 字符串按单词反转（必须保留所有空格）。
###   'I love you!  ' --> '  you! love I'
###   '    Hello, how are you?  Fine.    '

# reference: http://blog.csdn.net/raylee2007/article/details/48004489


## ！！！！！老师方法，先把每个单词字符反转，再把每个字符串反转，保留空格。 split()方法会丢空格。！！！！
def reverse0(str_list, start, end):
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]  ## 快速交换两个元素的值。
        start += 1
        end -= 1

sentence = '  Hello, how are you doing?   Fine.    '
str_list = list(sentence) # 字符串 --> 列表
print(str_list)
i = 0

while i < len(str_list):
    if str_list[i]:  # 如果不为空格，即一个单词的开始，记录一下。
        start = i
        #print('start', start)
        end = start + 1  # 从+1位置开始往后读，知道空格或结尾，知道单词的长度。
        while (end < len(str_list)) and str_list[end] != ' ':
            #print('end', end)
            end += 1
        reverse0(str_list, start, end - 1)
        i = end
    else:
        i += 1
str_list.reverse()
#print(str_list)
print(''.join(str_list))


## 其他方法。

#title('单词反转方法一： 对列表reverse')
def word_reverse1():
    title('单词反转方法一： 对列表reverse')
    s = input("please input some words: ")
    l = s.split()
    l.reverse() # 该方法没有返回值，但是会对列表的元素进行反向排序。
    result = ' '.join(l)
    return result


#title("单词反转方法二： 切片（好）")
def word_reverse2():
    title("单词反转方法二： 切片（好）")
    s = input("please input some words: ")
    l_r = s.split()[::-1]
    result = ' '.join(l_r)
    return result

#output = word_reverse2()
#print(output)




### 2. 打印100000 以内的所有素数。


### 3. 自己实现一个函数支持可变参数。

### 4. 自己实现函数解决汉诺塔。

### 5. 实现一个sort函数，通过参数指定排序函数用来实现按不同顺序进行排序。冒泡排序即可。