
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        min_angle = 6*minutes
        hour_angle = 30*(hour%12 + minutes/60)
        
        return min(abs(min(min_angle - hour_angle, (360 - min_angle) + (hour_angle))), \
                  abs(min(hour_angle - min_angle, (360 - hour_angle) + (min_angle))))
            

stime = time.time()
print(165 == Solution_1344().angleClock(hour = 12, minutes = 30))
print(75 == Solution_1344().angleClock(3, 30))
print(7.5 == Solution_1344().angleClock(3, 15))
print(155 == Solution_1344().angleClock(4, 50))
print(0 == Solution_1344().angleClock(12, 0))
print(76.5 == Solution_1344().angleClock(1, 57))
print(158.5 == Solution_1344().angleClock(8, 7))
print('elapse time: {} sec'.format(time.time() - stime))