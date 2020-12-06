import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        cnt = i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                j += 1
                cnt += 1
            i += 1
        
        return cnt

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result


stime = time.time()
sol = Solution()
res = sol.findContentChildren([10,9,8,7],[5,6,7,8])
print(res)
print('elapse time: {} sec'.format(time.time() - stime))
