# coding=utf-8
# 如何在一个for语句中迭代多个可迭代对象
# 并行：使用zip函数，将多个可迭代对象合并，每次迭代返回一个元组
# 串行：使用标准库的itertools.chain，它能将多个可迭代对象连接
from random import randint
from itertools import chain
chinese = [randint(60,100) for _ in xrange(40)]
math = [randint(60,100) for _ in xrange(40)]
english = [randint(60,100) for _ in xrange(40)]

for i in xrange(len(math)):
    chinese[i] + math[i] + english[i]

zip([1,2,3,4],['a','b','c','d','e'])#返回的是以元组为项的列表
totle = []
for c, m, e in zip(chinese, math, english):
    totle.append(c + m + e)
print totle

e1 = [randint(60,100) for _ in xrange(40)]
e2 = [randint(60,100) for _ in xrange(40)]
e3 = [randint(60,100) for _ in xrange(40)]
e4 = [randint(60,100) for _ in xrange(40)]
count = 0
for e in chain(e1, e2, e3, e4):
    if e >= 90:
        count += 1
print count
