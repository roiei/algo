
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = collections.defaultdict(list)
        mx = 0
        
        for num in range(1, n + 1):
            tot = sum([int(digit) for digit in str(num)])
            freq[tot] += num,
            mx = max(len(freq[tot]), mx)
        
        return len([k for k, v in freq.items() if len(v) == mx])


stime = time.time()
print(4 == Solution().countLargestGroup(n = 13))
print('elapse time: {} sec'.format(time.time() - stime))