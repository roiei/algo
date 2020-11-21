import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx = -1
        pos = collections.defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch] += i,

        for ch, idxs in pos.items():
            if not idxs or len(idxs) < 2:
                continue

            mx = max(mx, idxs[-1] - idxs[0] - 1)

        return mx


stime = time.time()
print(18 == Solution().maxLengthBetweenEqualCharacters('mgntdygtxrvxjnwksqhxuxtrv'))
print('elapse time: {} sec'.format(time.time() - stime))