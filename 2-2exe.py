# coding=utf-8
# 为元组中每个元素命名，提高程序可读性
# 正常我们使用引索(index)访问，降低了程序可读性

student = ('Jin',16, 'male', 'jin123@mail.com')

# 定义类似枚举类型，即数值常量。
# 使用标准库collections.nametuple替代内置tuple

NAME = 0
AGE =  1
SEX =  2
EMAIL = 3
NAME, AGE, SEX, EMAIL = xrange(4)

from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])#相当于一个类的工厂
s = Student('Jin',16, 'male', 'jin123@mail.com') #位置穿插
print s
s2 = Student(name= 'Jin',age=16,sex='male', email= 'jin123@mail.com')
#关键字穿插


# name
print student[NAME]
print s.name
# age
print student[AGE]
print s.age
# sex
print student[SEX]
print s.sex
# email
print student[EMAIL]
print s.email

print isinstance(s,tuple)
