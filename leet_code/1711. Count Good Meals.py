
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
    def countPairs(self, deliciousness: List[int]) -> int:
        power_of_twos = set([2**i for i in range(0, 22)])
        freqs = collections.Counter(deliciousness)
        cnt = 0
        visit = set()

        for val, freq in freqs.items():
            for po2 in power_of_twos:
                if po2 - val in freqs:
                    if po2 - val == val:
                        cnt += freq*(freq - 1)//2
                    else:
                        if po2 - val not in visit:
                            cnt += freq*freqs[po2 - val]
            visit.add(val)

        return cnt%(10**9 + 7)

    def countPairs(self, deliciousness):
        pots = set([2**i for i in range(0, 22)])
        freqs = collections.Counter(deliciousness)
        visited = set()
        cnt = 0

        for val, freq in freqs.items():
            for pot in pots:
                diff = pot - val
                if diff == val:
                    cnt += freq*(freq - 1)//2

                elif diff in freqs and diff not in visited:
                    cnt += freq*freqs[diff]

            visited.add(val)

        return cnt%(10**9 + 7)


stime = time.time()
print(4 == Solution().countPairs([1,3,5,7,9]))
print('elapse time: {} sec'.format(time.time() - stime))