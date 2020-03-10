
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def minAvailableDuration(self, slots1: [[int]], slots2: [[int]], duration: int) -> [int]:
        
        slots = sorted(slots1 + slots2, key=lambda p: p[0])

        fs, fe = slots.pop(0)
        overs = []

        while slots:
            ls, le = slots.pop(0)

            if fs <= ls < fe:
                start = max(fs, ls)
                end = min(fe, le)
                overs += (start, end),

            if fe < le:
                fs = ls
                fe = le

        for start, end in overs:
            length = end - start
            if length >= duration:
                return [start, start + duration]

        return []


stime = time.time()
print([60,68] == Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
print([] == Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
print('elapse time: {} sec'.format(time.time() - stime))