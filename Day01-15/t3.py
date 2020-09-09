username = input('请输入名字：')
password = input('请输入密码：')

if username == 'admin' and password == '123456':
    print('成功')
else:
    print('失败')

# 分段函数求值
x = float(input('请输入x(float) = '))
if x > 1:
    print(3 * x - 5)
elif 1 >= x >= -1:
    print(x + 2)
else:
    print(5 * x + 3)

# 英制单位英寸与公制单位厘米互换。
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit =='in' or unit == '英寸':
    print('%0.2f英寸 = %.2f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
else:
    print('error!')


# 百分制成绩转换为等级制成绩。
# 要求：
# 如果输入的成绩在90分以上（含90分）输出A；
# 80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；
# 60分以下输出E。

score = float(input('请输入成绩：'))
if score >= 90:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('E')

# 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and c + b > a:
    print('能构成三角形')
    print('周长=%.1f' % (a + b + c))
    p = (a + b + c) / 2
    print('面积=%.1f' % (p * (p - a) * (p - b) * (p - c)) ** 0.5)
else:
    print('不能构成三角形')
