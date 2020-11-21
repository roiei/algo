import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def heightChecker(self, heights: [int]) -> int:
        height_s = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if height_s[i] != heights[i]:
                cnt += 1
        return cnt

    def heightChecker(self, heights: [int]) -> int:
        return sum([1 if item1 != item2 else 0 for item1, item2 in zip(sorted(heights), heights)])


stime = time.time()
#print(3 == Solution().heightChecker([1,1,4,2,1,3]))
print(5 == Solution().heightChecker([5,1,2,3,4]))
print('elapse time: {} sec'.format(time.time() - stime))