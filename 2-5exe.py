# coding=utf-8
# 快速找到多个字典中的公共键(key)
# 利用集合(set)的交集操作
# 1.使用字典的viewkeys()方法，得到一个字典keys的集合
# 2.使用map()函数，得到所有字典的keys的集合
# 3.使用reduce函数，取所有字典的keys的集合的交集
from random import randint sample

sample('abcdefg', randint(3,6))#随机产生列表
s1 = {x:randint(1,4) for x in sample('abcdefg', randint(3, 6))}#随机产生字典

s2 = {x:randint(1,4) for x in sample('abcdefg', randint(3, 6))}#随机产生字典
s3 = {x:randint(1,4) for x in sample('abcdefg', randint(3, 6))}#随机产生字典
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print res

print s1.viewkeys(),s2.viewkeys(),s3.viewkeys()
# 取交集
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
# 拓展
#map(dict.viewkeys,[s1, s2, s3])
d = reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))
print d
