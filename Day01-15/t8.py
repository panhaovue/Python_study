from time import sleep


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
    # 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，
    def __init__(self, name, age):
        self.name = name  # self.__name = name 私有的
        self.age = age

    def study(self, course_name):
        print('%s正在学%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s可以看《飞驰人生》' % self.name)
        else:
            print('%s可以看《釜山行》' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu = Student('潘浩', 21)
    stu.study('计算机')
    stu.watch_movie()


class Test:

    def __init__(self, foo):
        # 属性名以单个下划线开头，属性是受保护的，protected
        # 属性名以两个下划线开头，属性是私有的 private
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main2():
    test = Test('hello')
    # 访问不到
    # test.__bar()          # AttributeError: 'Test' object has no attribute '__bar'
    # print(test.__foo)      # AttributeError: 'Test' object has no attribute '__foo'
    # 更换名字的规则仍然可以访问到它们
    test._Test__bar()
    print(test._Test__foo)


# 练习
# 练习1：定义一个类描述数字时钟。
class Clock(object):
    """数字时钟"""
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    main2()
    clock = Clock(17, 28, 40)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
