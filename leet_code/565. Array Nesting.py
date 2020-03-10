
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        g = collections.defaultdict(dict)
        for i, num in enumerate(nums):
            g[i][num] = True
        
        visited = set()
        mx = 0
        
        for num in nums:
            if num in visited:
                continue
            
            cnt = 0
            q = [num]
            visited.add(num)
            while q:
                u = q.pop(0)
                cnt += 1
                for v, linked in g[u].items():
                    if v in visited:
                        continue
                    visited.add(v)
                    q += v,
            
            mx = max(mx, cnt)
        return mx


stime = time.time()
print(4 == Solution().arrayNesting([5,4,0,3,1,6,2]))
print('elapse time: {} sec'.format(time.time() - stime))