# coding=utf-8
# 根据字典中值的大小，对字典中的项进行排序
# 使用内置函数sorted,利用zip将字典数据转换元组，传递sorted函数的参数
from random import randint

d = {x:randint(60,100) for x in 'xyzabc'}
print d
zip(d.values(), d.keys())
zip(d.itervalues(), d.iterkeys())#迭代版本，使用更节省空间
print sorted(zip(d.itervalues(), d.iterkeys()))

print sorted(d.items(),key=lambda x: x[1])
