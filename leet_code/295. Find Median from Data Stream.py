
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class MedianFinder:
    def __init__(self):
        self.data = []
        self.n = 0

    def addNum(self, num: int) -> None:
        idx = bisect.bisect_left(self.data, num)
        self.data.insert(idx, num)
        self.n += 1
        
    def findMedian(self) -> float:
        if self.n%2 == 0:
            return (self.data[self.n//2 - 1] + self.data[self.n//2])/2
        return self.data[self.n//2]


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))