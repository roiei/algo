
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def findLucky(self, arr: [int]) -> int:
        freq = collections.defaultdict(int)
        for num in arr:
            freq[num] += 1

        res = sorted([k for k, v in freq.items() if k == v])
        return res[-1] if res else -1



stime = time.time()
#print(2 == Solution().findLucky(arr = [2,2,3,4]))
print(3 == Solution().findLucky(arr = [1,2,2,3,3,3]))
print('elapse time: {} sec'.format(time.time() - stime))