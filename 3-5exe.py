# coding=utf-8
# 如何对迭代器做切片操作
# 使用标准库itertools.islice,它能返回一个迭代对象切片的生成器
from itertools import islice

f = open('/var/log/dmesg').readlines()
for line in f:
    print line

# islice(iterable, [start,] stop [,step])
for line in islice(f, 100, 300):
    print line
#一个参数表示结尾值,不支持负引索
islice(f, 100, None)#从100到结尾

l = range(20)
t = iter(l)
for x in islice(t, 5, 10):#t会被消耗掉，要重新申请迭代器
    print x
