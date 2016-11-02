# coding=utf-8
# 如何对字符串进行左，右，居中对齐
# 使用str.ljust(),str.rjust(), str.center()进行对齐
# 使用内置的format方法
s = 'abc'
print s.ljust(20)
print s.ljust(20, '=')# 以=作为填充物进行填充,字符靠左
print s.rljust(20)
print s.rjust(20, '=')# 以=作为填充物进行填充，字符靠右
print s.center(20)
print s.center(20, '=')#以=作为填充物，字符居中
print format(s, '<20')#做对齐
print format(s, '>20')
print format(s, '^20')#居中
