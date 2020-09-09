import sys

s1 = '\141\142\143\x61\x62\x63\n'
s2 = '\u6f58\u6d69'
s3 = '\u6f58'
print(s1, s2)

print(s2 not in s1)
print(s3 in s2)
print(s3 + s2)

# 字符串切片(从指定的开始索引到指定的结束索引) 一般来说区间都是[,)，即包括前面，不包括后面
s4 = '123456789'
print(s4[0])  # 1
print(s4[:2])  # 12       区间为[0，2)
print(s4[2:])  # 3456789  区间为[2,9)
print(s4[2::2])  # 3579     从2开始每隔2个取一个
print(s4[2::3])  # 369      从2开始每隔3个取一个
print(s4[::2])  # 13579
print(s4[::-1])  # 987654321   倒置
print(s4[-3:-1])  # 78     截取倒数第三位与倒数第一位之前的字符, 倒序的数字是从-1开始计算,并且范围表示前包含后不包含,即[), 所以结果为78
print(s4[-3:])  # 789         倒数第三位到结尾
print(s4[:-5:-1])  # 9876        逆序截取，先倒序, 间隔1, 截取

# 对字符串的处理
s5 = 'hello world'
print('字符串长度：%d' % len(s5))  # 11 通过内置函数len计算字符串的长度
print(s5.capitalize())  # Hello world  获得字符串首字母大写的拷贝
print(s5.title())  # Hello World  获得字符串首字母大写的拷贝,
print(s5.upper())  # HELLO WORLD  获得字符串变大写后的拷贝
print(s5.find('or'))  # 7   从字符串中查找子串所在位置
print(s5.find('rr'))  # -1  找不到时，返回-1
print(s5.index('or'))  # 7   与find相似,从字符串中查找子串所在位置
# print(s5.index('123'))         # 不同的是找不到子串时会引发异常,ValueError: substring not found
print(s5.startswith('He'))  # False, 检查字符串是否以指定的字符串开头,大小写也比较
print(s5.startswith('he'))  # True
print(s5.endswith('ld'))  # True 检查字符串是否以指定的字符串结尾
print(s5.center(50, '*'))  # 将字符串以指定的宽度居中放置,两侧填充指定的字符
print(s5.rjust(50, ' '))  # 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(s5.isdigit())  # False 检查字符串是否由数字构成
print(s5.isalpha())  # False 检查字符串是否以字母构成
print(s5.isalnum())  # False 检查字符串是否以数字和字母构成
s6 = '   stargazer'
print(s6)  # stargazer
print(s6.strip())  # stargazer   # 获得字符串修剪左右两侧空格之后的拷贝

a, b = 4, 5
# 格式化输出字符串
print('%d + %d = %d' % (a, b, a + b))
print('{0} + {1} = {2}'.format(a, b, a + b))
print(f'{a} + {b} = {a + b}')

# 数值类型(int, float)是标量类型，也就是说这种类型的对象没有可以访问的内部结构；
# 而字符串类型(str)是一种结构化的、非标量类型，所以才会有一系列的属性和方法。
# 列表（list），也是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，
# 定义列表可以将列表的元素放在[]中，多个元素用,进行分隔，可以使用for循环对列表元素进行遍历，
# 也可以使用[]或[:]运算符取出列表中的一个或多个元素。

list1 = [1, 2, 3, 5, 7]
print(list1)
list2 = ['hhh', 123] * 3  # 乘号表示列表元素的重复
print(list2)
print(len(list2))
print(list1[4])  # 索引
print(list1[-1])  # 倒数最后一个
print(list1[-3])  # 倒数第三个
# list1[2] = 300
print(list1)
# for i in range(len(list1)):
#     print(list1[i])

# 通过for循环遍历列表元素
# for j in list1:
#     print(j)
list1.remove(7)  # 存在就删除该元素
print(list1)
list1.pop(1)  # 从指定的位置删除元素
print(list1)
list2.clear()  # 清空列表元素, []

# append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。
list1.append(12)  # 添加元素，()里面可以是单个元素，也可以是列表、元组等。
list1.extend('13')  # 添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。
list1.insert(2, 222)  # listname.insert(index , obj) index 表示指定位置的索引值。insert() 会将obj插入到 listname 列表第 index 个元素的位置。
print(list1)

# 列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
fruits = ['apple', 'watermelon', 'pear', 'grape']
fruits += ['strawberry', 'orange']
print(fruits)
fruits1 = fruits[:]  # 可以通过完整切片操作来复制列表, 同fruits1 = fruits
fruits2 = fruits[1:4]  # ['watermelon', 'pear', 'grape'], 区间为[1,4)
fruits3 = fruits[-3:-1]  # ['grape', 'strawberry'], 区间为[-3,-1)
fruits4 = fruits[::-1]  # 倒置

# 对列表的排序操作, sorted()默认按照字母表顺序排序
# sorted函数返回列表排序后的拷贝不会修改传入的列表, 函数的设计就应该像sorted函数一样尽可能不产生副作用
fruits5 = sorted(fruits)  # 按字母A-Z顺序排列
fruits6 = sorted(fruits, reverse=True)  # 按Z-A顺序排列
fruits7 = sorted(fruits, key=len)  # 通过key关键字参数指定根据字符串长度进行排序
fruits.sort(reverse=True)  # 给列表对象发出排序消息直接在列表对象上进行排序
print(fruits5)
print(fruits6)
print(fruits7)

# 可以使用列表的生成式语法来创建列表, 它的缺陷是所有数据都在内存中，如果有海量数据的话将会非常耗内存。
f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABC' for y in '12']  # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
print(f)

f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数

# Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。

# 元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，不同之处在于元组的元素不能修改
t = ('panhao', 21, '男')
print(t)
print(t[0])
print(t[-1])
# 遍历元组中的值
# for v in t:
#     print(v)
print(t[::-1])  # 倒置
# t[0] = 'li'           # TypeError: 'tuple' object does not support item assignment
t = ('li')  # 变量t重新引用了新的元组，原来的元组将被垃圾回收
person = list(t)  # 将元组转换成列表
# print(person)           # ['l', 'i']
person[0] = 'li'
person[1] = '12'
# person[2] = 'cc'        IndexError: list assignment index out of range
print(person)

fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)  # 将列表转换成元组
print(fruits_tuple)

print(sys.getsizeof(fruits_list))  # 88
print(sys.getsizeof(fruits_tuple))  # 72

# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
set1 = {1, 2, 3, 5, 6, 8}
print(set1)
print('Len = %d' % len(set1))
set2 = set(range(10))  # 创建集合的构造器语法(面向对象部分会进行详细讲解)
set3 = set((11, 21, 13, 24))
print(set2, set3)
set4 = {num for num in range(1, 100) if num % 3 == 0 and num % 5 == 0}  # 创建集合的推导式语法(推导式也可以用于推导集合)
print(set4)

# 向集合添加元素和从集合删除元素。
set1.add(10)
set1.update([11, 21])  # add, update都是在结尾添加元素
set1.discard(1)  # 删除元素1
set1.remove(2)  # 删除元素2
# if 5 in set1:
#     set1.discard(5)          # 或者 set1.remove(5)
set1.pop()  # 删除第一个元素

# 集合的成员、交集、并集、差集等运算。

print(set1 & set2)  # {8, 5, 6}
# print(set1.intersection(set2))
print(set1 | set2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21}
# print(set1.union(set2))
print(set1 - set2)  # {10, 11, 21}
# print(set1.difference(set2))
print(set1 ^ set2)  # {0, 1, 2, 3, 4, 7, 9, 10, 11, 21}
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)  # False
# print(set2.issubset(set1))
print(set3 <= set1)  # False
# print(set3.issubset(set1))
print(set1 >= set2)  # False
# print(set1.issuperset(set2))
print(set1 >= set3)  # False
# print(set1.issuperset(set3))


# 字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，
# 与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。

# 创建字典的字面量语法
scores = {'潘浩': 99, '李凤英': 77, '陈圆圆': 88}
print(scores['潘浩'])  # 通过键可以获取字典中对应的值
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3)  # {'one': 1, 'two': 2, 'three': 3}
items2 = dict(zip(['a', 'b', 'c'], '123'))  # 通过zip函数将两个序列压成字典
items3 = {num: num ** 2 for num in range(1, 10)}

# 更新字典中的元素
scores['潘浩'] = 97
scores.update(冷面=67, 方启鹤=85)

if '潘浩' in scores:
    print(scores['潘浩'])
print(scores.get('潘浩'))
print(scores.popitem())  # 删除字典中的元素, 删除最后一个元素
print(scores.pop('陈圆圆'))  # 删除对应的元素,
scores.clear()  # 清空字典

# 练习1：在屏幕上显示跑马灯文字。
import os
import time


def main():
    content = '潘浩是傻子。。。连研究生也考不上。。'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code


# 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename, has_dot=False):
    suffix = ''
    index = 0
    if '.' in filename:
        has_dot = True
        index = filename.find('.')
    index += 1
    while has_dot:
        suffix += filename[index]
        index += 1
        if index == len(filename):
            break
    if has_dot:
        return suffix
    return '没有后缀'


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for m in x:
        if m > m1:
            m2 = m1
            m1 = m
        elif m2 < m < m1:
            m2 = m
    return m1, m2


# 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    # 判断指定的年份是不是闰年, 闰年返回True平年返回False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    # 计算传入的日期是这一年的第几天
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
    # True就是闰年，是day_of_month[1]; False是平年，是day_of_month[0]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


# 练习6：打印杨辉三角。
def pascal_triangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


# 约瑟夫环问题
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
# 个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
# 报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，
# 问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
def josephus_problem():
    persons = [True] * 30
    count, index, number = 0, 0, 0
    while count < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                number = 0
                count += 1
        index += 1
        index %= 30
    for i in persons:
        print('基' if i else '非', end='')


if __name__ == '__main__':
    print(generate_code())
    print(get_suffix('asdsad.txt'))
    print(get_suffix('asdsad'))
    x = [3, 12, 35, 45, 6, 34, 8, 23, 66, 124, 12]
    print(max2(x))
    print(which_day(2100, 7, 21))
    print(which_day(2000, 1, 1))
    pascal_triangle()
    josephus_problem()
