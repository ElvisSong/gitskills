# coding=utf-8
# 如何去掉字符串中不需要的字符
# 使用str.strip(),str.lstrip(),str.rstrip()去掉头尾，左端，右端
# 删除固定位置字符使用切片加拼接的方式
# 字符串的replace()或者正则表达式的re.sub()方法
# 字符串translate()方法，可以同时删除多种不同字符
s = '    abc   123   '
print s.strip()# 去掉前后空白字符，带参数则去掉参数字符
print s.lstrip()# 去掉左端
print s.rstrip()# 去掉右端
s = '---adc+++'
print s.strip('-+')
s = 'abc:123'
print s[:3]+ s[4:]

s = '\tabc\t123\txyz'
s.replace('\t','')
s = '\tabc\t123\txyz\ropd\r'
import re 
re.sub('[\t\r]', '', s)

s = 'abc1234556xyz'
import string
string.maketrans('abcxyz', 'xyzabc')
s.translate(string.maketrans('abcxyz', 'xyzabc'))
s = '\tabc\t123\txyz\ropd\r'
s.translate(None, '\t\r')
