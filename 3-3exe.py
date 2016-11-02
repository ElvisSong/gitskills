# coding=utf-8
# 使用生成器函数实现可迭代对象
# 包含yield语句就是生成器函数

def f():
    print 'in f(),1'
    yield 1

    print 'in f(),2'
    yield 2

    print 'in f(),3'
    yield 3

g= f()

for x in g:
    print x
#g实现了g.__iter__()接口,返回的是g自身

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1, 100):
    print x
