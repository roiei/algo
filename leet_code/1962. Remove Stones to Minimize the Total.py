import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import math
import functools
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def dfs(piles, k):
            if k == 0:
                return sum(piles)

            mn = float('inf')
            for i in range(len(piles)):
                next_file = piles[:]
                next_file[i] = math.floor(next_file[i]/2 + 0.5)
                mn = min(mn, dfs(next_file, k - 1))

            return mn

        mn = dfs(piles, k)
        return mn

    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-num for num in piles]
        heapq.heapify(piles)

        while k:
            num = heapq.heappop(piles)
            heapq.heappush(piles, num//2)
            k -= 1

        return -sum(piles)


stime = time.time()
print(12 == Solution().minStoneSum(piles = [5,4,9], k = 2))
print(12 == Solution().minStoneSum(piles = [4,3,6,7], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))