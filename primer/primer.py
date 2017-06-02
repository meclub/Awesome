# coding=utf-8

from __future__ import print_function

import types

import module
from module import Bike
from module import MountainBike
from module import Fib
from module import Github

# Basic type
import functools

a = -8000
b = 0x123
c = 1.2e5
print(a, b, c)

# Char \
print(r'\\\\\\\\')
print('I\'m \\ok\n\t')
print('''line1
line2
line3
''')
print(True, False)
print(True or False, True and False, not True)
print(None)

a = 'ABC'
b = a
a = 'DEF'
print(a, b)

NUM = 1000
print(NUM)

print('这是一句中文')

# List
lists = ['a']
print(lists)

lists.append('b')
print(lists)

lists.insert(1, 'c')
lists.append('d')
lists.append('e')
print(lists)

lists.pop()
print(lists)
print(lists[0], lists[3])

# Tuple
tuples = (0, 1, 2)
print(tuples)

t = (1,)
print(t)

# Loop
ages = (17, 20)
for age in ages:
    if age > 18:
        print("成年人")
    else:
        print("未成年")

# Dict 空间换时间
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d['b'])

# Set
s = {0, 1, 2}
print(s)

# Function
print(abs(-100))


def abs_ex(num):
    if not isinstance(num, (int, float)):
        raise TypeError('Bad operand type')
    if num > 0:
        return num
    else:
        return -num


print(abs_ex(-100))


# print(abs_ex('abc'))

def get_rect(size):
    if not isinstance(size, (int, float)):
        raise TypeError('Bad operand type')
    return size, size, size, size


print(get_rect(100))

# 切片
print(ages[0:1])
print(ages[1:2])
print(ages[:2:2])

# Iteration
for key, value in d.iteritems():
    print(key, value)

# Get
for i, value in enumerate(ages):
    print(i, value)

# Create list
print([x * x for x in range(1, 6) if x % 2 == 0])
print([m + n for m in 'ABC' for n in "abc"])
print([age > 18 for age in ages])


# Generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print(fib(10))
for n in fib(10):
    print(n)


# Map
def f(x):
    return x * x


print(map(f, [1, 2, 3, 4]))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def first_up(s):
    if not isinstance(s, str):
        return s
    return s[:1].upper() + s[1:].lower()


print(map(first_up, [1111, 'EFedda', 'A', 'c']))
print(map(first_up, ['adam', 'LISA', 'barT']))


# Reduce
def add(x, y):
    return 10 * x + y


def multiplication(x, y):
    return x * y


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(list):
    return reduce(multiplication, list)


print(prod([1, 2, 3, 4, 5]))

print(reduce(add, [1, 3, 5, 7, 9]))


# Filter
def not_prime(num):
    if not isinstance(num, int):
        return num

    if num == 1:
        return False

    n = 2
    while n < num:
        if num % n == 0:
            return False
        n += 1

    return True


print(filter(not_prime, range(1, 101)))


# Sorted
def cmp_ignore_case(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return 0

    u1 = s1.lower();
    u2 = s2.lower();
    return u1 > u2


print(sorted([1, 2, 3, 4, 5]))
print(sorted([1, 2, 3, 4, 5], reverse=True))
print(sorted(['abbc', 'DDDD', 'eeere']))
print(sorted(['abbc', 'DDDD', 'eeere'], cmp_ignore_case))

# 匿名函数
print(map(lambda x: x * x, [1, 2, 3, 6]))


# 装饰器
def logDecorator(func):
    def wrapper(*args, **kw):
        print('call %s before' % func.__name__)
        func(*args, **kw)
        print('call %s after' % func.__name__)

    return wrapper


@logDecorator
def log(s):
    print(s)


log("bean")

# 偏函数
int2 = functools.partial(int, base=2)
print(int('100000'))
print(int2('100000'))

# Array
company = ['珠海扬智电子科技有限公司']
company_str = company[0]
print(company)

# Module
module.test()

# Class
bike = Bike("美利达", 1000)
print(Bike)
print(bike)
print(bike.name)
print(bike.price)
print(bike.get_level())

mountainBike = MountainBike("捷安特", 1500)
print(mountainBike.name)
print(mountainBike.price)
print(mountainBike.get_level())

# Object type
print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print(type(bike))
print("asd is type string:", type('asd') == types.StringType)
print("111 is type string:", isinstance(111, str))

print("bike isinstance MountainBike:", isinstance(bike, MountainBike))
print("mountainBike isinstance Bike:", isinstance(mountainBike, Bike))

print("dir bike", dir(bike))

print("bike has attr price", hasattr(bike, 'price'))
print("bike has attr road", hasattr(bike, 'road'))
print("bike set attr price")
setattr(bike, 'price', 600)
print("bike has attr road", getattr(bike, 'price', 500))

# slots
print (bike.__slots__)

# Property
bike.color = 'green'
print(bike.color)

# 多重继承
mountainBike.run()

# 定制类, 例如str, iter, getitem,
print (bike)
print ("Fib 100:")
for n in Fib():
    print(n)

# getattr
print(Github().user.avater)
print(Github().users('kylingo').repos)

# callable
a = Github()
a()