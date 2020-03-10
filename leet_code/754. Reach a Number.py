import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reachNumber(self, target):
        target = abs(target)
        cur = cnt = 0
        unit = 1
        while cur < target or 1 == abs(cur-target)%2:
            cur+= unit
            unit+= 1
            cnt+= 1
        return cnt


    # timeout
    def reachNumber(self, target: int) -> int:
        if target == 0:
            return 0
        
        q = [(0, 1)]
        visited = set()
        
        while q:
            cur, step = q.pop(0)
            for offset in [-1, 1]:
                next = cur + offset*step
                print('next = {:2}, cur = {:2}, step = {:2}'.format(next, cur, step))
                if next == target:
                    return step
                q += (next, step + 1),
                visited.add(next)
        
        return -1


stime = time.time()
sol = Solution()
print(3 == sol.reachNumber(2))
print('elapse time: {} sec'.format(time.time() - stime))
