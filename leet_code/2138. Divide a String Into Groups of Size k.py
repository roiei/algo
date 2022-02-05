import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []

        i = 0
        while i < n:
            pad = k - len(s[i:i + k])
            res += s[i:i + k] + fill*pad,
            i += k

        return res


stime = time.time()
print(["abc","def","ghi","jxx"] == Solution().divideString(s = "abcdefghij", k = 3, fill = "x"))
print('elapse time: {} sec'.format(time.time() - stime))