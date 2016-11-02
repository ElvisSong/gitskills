# coding=utf-8
# 在列表，字典，集合中根据条件筛选数据
# 过滤列表负数，筛选字典中值高于90的项，筛选出集合中能被3整除的数
# 使用函数式编程，列表解析，字典解析，集和解析
from random import randint

data = [randint(-10,10) for _ in xrange(10)]
print filter(lambda x:x >= 0 ,data)

data2 = [x for x in data if x >= 0 ]#列表解析时间更短
print data2

d = {x:randint(60,100) for x in xrange(1,21)}
d2 = {k:v for k,v in d.iteritems() if v > 90}
print d2

s = set(data)
s2 = {x for x in s if x % 3 == 0}
print s2
