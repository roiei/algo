import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        def search(nums, l, r, tgt):
            while l <= r:
                m = (l+r)//2
                if nums[m] == tgt:
                    return m
                if nums[m] > tgt:
                    r = m-1
                else:
                    l = m+1
            return l
        
        if not stones:
            return -1
        stones.sort()
        while len(stones) > 1:
            r = stones.pop()
            l = stones.pop()
            left = r - l
            if left == 0:
                continue
            if left > 0:
                idx = search(stones, 0, len(stones)-1, left)
                stones.insert(idx, left)
        return 0 if not stones else stones[0]


stime = time.time()
#print(1 == Solution().lastStoneWeight([2,7,4,1,8,1]))
print(0 == Solution().lastStoneWeight([2, 2]))
print('elapse time: {} sec'.format(time.time() - stime))

