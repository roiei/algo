
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import bisect
import collections
import operator


class ProductOfNumbers:

    def __init__(self):
        self.pro = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.pro += self.pro[-1]*num,
        else:
            self.pro = [1]

    def getProduct(self, k: int) -> int:
        if k >= len(self.pro):
            return 0
        
        return self.pro[-1]//self.pro[-k - 1]
        

    def getProduct2(self, k):
        if k >= len(self.A):
            return 0
        return self.A[-1] / self.A[-k - 1]
        
            
stime = time.time()
ins = zip(["add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"], [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]], [None,None,None,None,None,20,40,0,None,32])
pn = ProductOfNumbers()

for op, param, ans in ins:
    ret = None
    if op == 'add':
        ret = pn.add(param[-1])
    elif op == 'getProduct':
        ret = pn.getProduct(param[-1])

    if ans != ret:
        print('False')
        break
else:
    print('True')

print('elapse time: {} sec'.format(time.time() - stime))