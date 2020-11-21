import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:
        pos = collections.defaultdict(int)
        for n, s, e in trips:
            pos[s] += n
            pos[e] -= n
        
        pos = sorted(pos.items(), key=lambda p: p[0])
        
        cur = 0
        for time, num in pos:
            cur += num
            if cur > capacity:
                return False
    
        return True


stime = time.time()
print(True == Solution().carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))
print('elapse time: {} sec'.format(time.time() - stime))