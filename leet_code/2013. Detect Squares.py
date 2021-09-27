
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class DetectSquares:
    def __init__(self):
        self.cnt = collections.defaultdict(int)
        self.coords = set()

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1
        self.coords.add(tuple(point))

    def count(self, point: List[int]) -> int:
        cx, cy = point
        
        num = 0
        for x, y in self.coords:
            if abs(cx - x) == 0 or abs(cx - x) != abs(cy - y):
                continue
            
            num += self.cnt[(x, y)] * self.cnt[(cx, y)] * self.cnt[(x, cy)]
        
        return num


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))