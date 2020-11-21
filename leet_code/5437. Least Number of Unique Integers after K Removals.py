import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: [int], k: int) -> int:
        freq = collections.Counter(arr)
        freq = sorted(freq.items(), key=lambda p: p[1])
        left = set()

        for key, v in freq:
            for i in range(v):
                if k:
                    k -= 1
                    continue
                left.add(key)

        return len(left)
    


stime = time.time()
print(2 == Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
print('elapse time: {} sec'.format(time.time() - stime))