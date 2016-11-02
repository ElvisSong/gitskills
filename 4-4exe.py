# coding=utf-8
# 如何将多个小字符串拼接成一个大字符串
# 使用迭代，连续使用+(调用了 str.__add__)拼接。使用str.join()拼接
s1 = 'abcdefg'
s2 = '123456'

pl = [s1, s2]
s = ''
for p in pl:
    s += p
print s#这种方式存在巨大的浪费，每次s都要被释放，复制

print ','.join(pl)#以，作为分隔符，参数为可迭代对象
print ''.join(pl)#无分隔符
l = ['abc', 123, 45, 'xyz']
''.join(str(x) for x in l)# 一个生成器表达式
