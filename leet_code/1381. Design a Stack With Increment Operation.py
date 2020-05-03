
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class CustomStack:

    def __init__(self, maxSize: int):
        self.data = []
        self.max_size = maxSize
        self.num = 0


    def push(self, x: int) -> None:
        if self.num >= self.max_size:
            return

        self.data += x,
        self.num += 1
        

    def pop(self) -> int:
        if self.num == 0:
            return -1

        ret = self.data.pop()
        self.num -= 1
        return ret
        

    def increment(self, k: int, val: int) -> None:
        mx = min(self.num, k)
        for i in range(mx):
            self.data[i] += val
        


ops = ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
params = [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
outputs = [None,None,None,2,None,None,None,None,None,103,202,201,-1]

obj = None
for op, param, output in zip(ops, params, outputs):
    ret = None
    if op == 'CustomStack':
        obj = CustomStack(param[0])
        continue
    elif op == 'push':
        ret = obj.push(param[0])
    elif op == 'pop':
        ret = obj.pop()
    elif op == 'increment':
        ret = obj.increment(*param)

    if output != ret:
        print('ERROR @ output {}, ret {}, op {}, parma {}'.format(output, ret, op, param))
