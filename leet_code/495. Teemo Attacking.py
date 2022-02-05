import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        pos = collections.defaultdict(int)
        
        for start in timeSeries:
            pos[start] += 1
            pos[start + duration] -= 1
        
        pos = sorted(pos.items(), key=lambda p: p[0])
        overlap_cnt = 0
        elapse = 0
        pretime = 0

        for time, cnt in pos:
            if overlap_cnt > 0:
                elapse += time - pretime
        
            overlap_cnt += cnt
            pretime = time
            
        return elapse

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        points = []
        for time in timeSeries:
            points += (time, 1),
            points += (time + duration, -1),
        
        points.sort(key=lambda p: p[0])
        
        pre_point = points[0][0]
        level = 0        
        duration = 0
        
        for point, inc in points:
            if level == 0 and inc:
                pre_point = point
                
            level += inc
            
            if level == 0:
                duration += point - pre_point
            
        return duration

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        points = []
        for time in timeSeries:
            points += (time, 1),
            points += (time + duration, -1),
        
        points.sort(key=lambda p: p[0])
        
        pre_point = points[0][0]
        level = 0        
        duration = 0
        
        for point, inc in points:
            if level > 0:
                duration += point - pre_point

            pre_point = point
            level += inc
            
        return duration


stime = time.time()
#print(2 == Solution().findPoisonedDuration(timeSeries = [1], duration = 2))
print(4 == Solution().findPoisonedDuration(timeSeries = [1,4], duration = 2))
print('elapse time: {} sec'.format(time.time() - stime))