# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
for num in range(100, 1000):
    low = int(num % 10)
    mid = int(num % 100 / 10)
    high = int(num / 100)
    if num == low ** 3 + mid ** 3 + high ** 3:
        print('%d是仙花数' % num)

# 正整数的反转
num = int(input('输入一个正整数：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)

# 百钱百鸡问题。
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('🐓：%d, 母鸡：%d, 小鸡：%d' % (x, y, z))

# CRAPS赌博游戏。
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续摇骰子，直到分出胜负。

from random import randint


def craps():
    money = 1000
    times = 0
    first = 0
    while money > 0:
        times += 1
        print('你的余额为%d' % money)
        try:
            debt = int(input('下注：'))
        except ValueError as e:
            print(e, '输入整数')
        else:
            count = randint(1, 6) + randint(1, 6)
            if times == 1:
                first = count
                if count == 7 or count == 11:
                    money += debt
                    print('点数为:%d, 你赢了, 余额: %d' % (count, money))
                elif count == 2 or count == 3 or count == 12:
                    money -= debt
                    print('点数为:%d, 你输了, 余额: %d' % (count, money))
                else:
                    print('平手')
                    continue
            else:
                if count == first:
                    money += debt
                    print('点数为:%d, 你赢了, 余额: %d' % (count, money))
                elif count == 7:
                    money -= debt
                    print('点数为:%d, 你输了, 余额: %d' % (count, money))
                else:
                    print('平手')
                    continue
    print('你玩了%d局，破产，结束！' % times)


# 生成斐波那契数列的前20个数。
# 斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和
def Fibonacci():
    num1 = 1
    num2 = 1
    print(num1)
    print(num2)
    for i in range(1, 20):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3


# 找出10000以内的完美数。
# 它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
# 判断一个数是不是完美数
import math


def checkPerfectNumber(num) -> bool:
    result = 0
    if num > 0:
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                if 1 < factor != num // factor:
                    result += num // factor
        if result == num and num != 1:
            return True
    else:
        return False


# 输出100以内所有的素数。
# 说明：素数指的是只能被1和自身整除的正整数（不包括1）。
def prime_numbers():
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


if __name__ == '__main__':
    print(checkPerfectNumber(-1))
    prime_numbers()
