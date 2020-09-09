from math import pi

a = 10
b = 12.21
c = 'ewf'
d = 1 + 2j

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'complex'>

a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))
# 上面的print函数中输出的字符串使用了占位符语法，其中%d是整数的占位符，%f是小数的占位符，
# %%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%）

flag0 = 1 == 1
flag1 = 3 < 2

print('flag0 = ', flag0)
print('flag1 = ', flag1)

# 华氏温度转换为摄氏温度。转换公式为：$C=(F - 32) \div 1.8$。

F = float(input('请输入华氏温度(float)：'))
C = (F - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (F, C))

# 输入圆的半径计算计算周长和面积。
radius = float(input('请输入半径(float)：'))
perimeter = 2 * pi * radius
area = pi * radius * radius
print('周长:%.2f, 面积:%.2f' % (perimeter, area))

# 输入年份判断是不是闰年。
year = int(input('请输入年份：'))
if year <= 0:
    print('error!')
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('闰年')
else:
    print('平年')
