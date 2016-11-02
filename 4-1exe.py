# coding=utf-8
# 如何拆分含有多种分隔符的字符串
# 1.连续使用str.split()方法，每次处理一种分割符号
# 2.使用正则表达式的re.split()方法，一次性拆分字符串
import re
def mySplit(s, ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    return [x for x in res if x ]

s = 'ab;cd|efg,hij\tkl,mnop\tqrstu|vwx;yz'
print mySplit(s, ';,|\t')

out = re.split(r'[,;\t|]+', s)
print out
