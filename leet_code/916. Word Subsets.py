
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def wordSubsets(self, A: [str], B: [str]) -> [str]:
        res = []
        freq_b = collections.defaultdict(int)

        for b in B:
            freq = collections.Counter(b)
            for k, v in freq.items():
                freq_b[k] = max(freq_b[k], v)

        for a in A:
            freq_a = collections.Counter(a)

            for k, v in freq_b.items():
                if v > freq_a[k]:
                    break
            else:
                res += a,
        
        return res


stime = time.time()
print(["facebook","google","leetcode"] == Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], B = ["e","o"]))
print('elapse time: {} sec'.format(time.time() - stime))

