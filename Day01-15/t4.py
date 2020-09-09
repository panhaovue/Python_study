# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
# for i in range(0, 101, 2):
#     print(i)

# 实现1~100之间的偶数求和
odd = 0
for i in range(0, 101, 2):
    odd += i
print(odd)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print()

# 猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
# 计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

import random

count = 0

answer = random.randint(1, 100)
while True:
    try:
        number = int(input('请输入一个数（0-100）：'))
    except ValueError as e:
        print('请输入整数')
        continue
    else:
        count += 1
        if number > answer:
            print('大了')
        elif number < answer:
            print('小了')
        else:
            print('恭喜')
            break
print('你猜了%d次' % count)

# 输入一个正整数判断是不是素数。素数指的是只能被1和自身整除的大于1的整数。
from math import sqrt
try:
    number1 = int(input('输入一个正整数:'))
except ValueError as e:
    print('请输入整数')
else:
    end = int(sqrt(number1))
    for i in range(2, end + 1):
        if number1 % i == 0:
            print('不是素数')
            break
        print('素数')
        break

# 输入两个正整数，计算它们的最大公约数和最小公倍数。
# 两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

x = int(input('x = '))
y = int(input('y = '))
# 如果如果x大于y就交换x和y的值
if x > y:
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('最大公约数:%d' % factor)
        print('最小公倍数:%d' % (x * y // factor))

# 打印如下所示的三角形图案
for i in range(6):
    for j in range(i + 1):
        print('*', end='')
    print()
