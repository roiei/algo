
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 3 8 7 1 4
        # 
        # 1 3 4 7 8
        # l       r = 9 <= 9 -> +1
        #
        # 1 3 4 7 8
        #   l   r   = 10 > 9 -> +1
        #
        # 1 3 4 7 8
        #   l r

        people.sort()
        l = 0
        r = len(people) - 1
        cnt = 0

        while l <= r:
            if l != r:
                s = people[l] + people[r]
            else:
                s = people[l]

            if s <= limit: # cover 2 people
                cnt += 1
                l += 1
                r -= 1
            else:
                if people[r] <= limit: # cover fat one
                    cnt += 1
                r -= 1

        return cnt


stime = time.time()
print(1 == Solution().numRescueBoats(people = [1,2], limit = 3))
print(3 == Solution().numRescueBoats(people = [3,2,2,1], limit = 3))
print(4 == Solution().numRescueBoats(people = [3,5,3,4], limit = 5))
print(3 == Solution().numRescueBoats([3,8,7,1,4], 9))

print('elapse time: {} sec'.format(time.time() - stime))