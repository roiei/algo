import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.freq1 = collections.Counter(nums1)
        self.freq2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        prev_val = self.nums2[index]

        self.freq2[prev_val] -= 1
        if self.freq2[prev_val] == 0:
            del self.freq2[prev_val]

        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.freq1:
            diff = tot - num
            if diff in self.freq2:
                cnt += self.freq2[diff]*self.freq1[num]
    
        return cnt


ops = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
params = [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
output = [None, 8, None, 2, 1, None, None, 11]
ins = zip(ops, params, output)
obj = None
res = []

for op, param, out in ins:
    if op == "FindSumPairs":
        obj = FindSumPairs(*param)
        res += [None]
    elif op == "count":
        res += obj.count(*param),
    elif op == "add":
        res += obj.add(*param),

    if out != res[-1]:
        print('op = {} is Failed: return = {}, exp = {}'.format(op, res, out))



stime = time.time()
#print(1 == Solution().minSwaps("111000"))
print('elapse time: {} sec'.format(time.time() - stime))