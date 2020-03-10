import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_s = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if height_s[i] != heights[i]:
                cnt += 1
        return cnt


stime = time.time()
print(Solution().heightChecker([1,1,4,2,1,3]))
print('elapse time: {} sec'.format(time.time() - stime))