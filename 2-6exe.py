# coding=utf-8
# 如何让字典保持有序
# 使用collections.OrderedDict替代内置字典Dict,依次将选手成绩存入OrderedDict
d = {}
d['Jim']= (1, 35)
d['Leo']= (2, 37)
d['Bob']= (3, 40)

from collections import OrderedDict
d = OrderedDict()
d['Jim']= (1, 35)
d['Leo']= (2, 37)
d['Bob']= (3, 40)
for k in d :print k
# 模拟竞赛系统
from time import time
from random import randint

d2 = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start,
    d2[p]= (i + 1, end - start)

print 
print '-'*20
for k in d2:
    print k, d2[k]
