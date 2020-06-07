import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.num = 1
        self.pos = 0
        self.cur = homepage
        self.history += homepage,

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pos + 1]
        self.num = self.pos + 1

        self.history += url,
        self.num += 1
        self.pos += 1
        self.cur = url

    def back(self, steps: int) -> str:
        while self.pos > 0 and steps:
            self.pos -= 1
            self.cur = self.history[self.pos]
            steps -= 1

        return self.cur

    def forward(self, steps: int) -> str:
        while self.pos + 1 < self.num and steps:
            self.pos += 1
            self.cur = self.history[self.pos]
            steps -= 1

        return self.cur

        
params = list(zip(["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"], [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]], [None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]))

bh = None
stime = time.time()
for op, param, out in params:
    print(op, param)

    ret = None
    if op == 'BrowserHistory':
        #print('BrowserHistory')
        bh = BrowserHistory(param[0])
    elif op == 'visit':
        #print('visit')
        ret = bh.visit(param[0])
    elif op == 'back':
        #print('back')
        ret = bh.back(param[0])
    elif op == 'forward':
        #print('forward')
        ret = bh.forward(param[0])

    #print(op, ret, out)

    if ret != out:
        print('op = ', op, ' ret = ', ret, ' out = ', out)

print('elapse time: {} sec'.format(time.time() - stime))
