
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        if not time:
            return 0

        cnt = 0
        freq = collections.defaultdict(int)
        for t in time:
            print(t)
            print(freq)
            print((60 - t)%60)
            cnt += freq[(60 - t)%60]
            freq[t%60] += 1
            print(cnt)
            print()

        return cnt


stime = time.time()
print(3 == Solution().numPairsDivisibleBy60([30,20,150,100,40]))
print('elapse time: {} sec'.format(time.time() - stime))