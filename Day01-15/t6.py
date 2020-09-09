# 实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    """求最大公约数"""
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


# 实现判断一个数是不是回文数的函数。
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


# 实现判断一个数是不是素数的函数。
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input('x = '))
    print(is_palindrome(x))
    num = int(input('num = '))
    print(is_prime(num))
