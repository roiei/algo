import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class FrontMiddleBackQueue:
    def __init__(self):
        self.nums = []        

    def pushFront(self, val: int) -> None:
        self.nums.insert(0, val)        

    def pushMiddle(self, val: int) -> None:
        self.nums.insert(len(self.nums)//2, val)

    def pushBack(self, val: int) -> None:
        self.nums += val,

    def popFront(self) -> int:
        return self.nums.pop(0) if self.nums else -1

    def popMiddle(self) -> int:
        return self.nums.pop((len(self.nums) - 1)//2) if self.nums else -1

    def popBack(self) -> int:
        return self.nums.pop() if self.nums else -1


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))
