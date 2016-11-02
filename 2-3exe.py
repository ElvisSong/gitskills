# coding=utf-8
# 统计序列中元素出现的频度
# 找出某序列中出现次数最高的3个元素，显示出现次数
# 对英文文章进行词频统计，找到出现次数最多的单词，显示出现次数

from random import randint

data = [randint(0,20) for _ in xrange(30)]
# 最终统计结果是字典

c = dict.fromkeys(data,0)

for x in data:
    c.[x] += 1

print c

# 
from collections import Counter
c2 = Counter(data)
# 使用most_common,找到出现次数最高的元素
c2.most_common(3)

import re
txt = open('READMD.md').read()
c3 = Counter(re.split('\W+', txt))
print c3
c3.most_common(10)
