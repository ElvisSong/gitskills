# coding=utf-8
# 如何实现保存历史记录的功能
# 使用标准库collections中的deque,它是一个双端循环队列
# 程序退出前，使用文将将其保存起来，使用pickle
from random import randint
from collections import deque
import pickle

N = randint(0, 100)
history = deque([], 5)

def guess(k):
    if k == N:
        print 'right'
    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False

while True:
    line = raw_input('please guess a number:')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)

pickle.dump(history, open('history', 'w'))
pickle.load(open('history'))
