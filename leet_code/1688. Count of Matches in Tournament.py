import time
from util.util_list import *
from typing import List


class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        
        while n > 1:
            cnt += n//2
            n = n//2 + n%2
        
        return cnt
            

stime = time.time()
print(6 == Solution().numberOfMatches(7))
print('elapse time: {} sec'.format(time.time() - stime))
