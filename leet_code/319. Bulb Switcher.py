
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def bulbSwitch(self, n: int) -> int:
        if not n:
            return 0
        bulbs = [1]
        for i in range(2, n + 1):
            cnt = 1

            for div in range(2, i//2 + 1):
                if i%div == 0:
                    cnt += 1
            
            if cnt%2 == 0:
                bulbs += 1,
            else:
                bulbs += 0,
        return bulbs.count(1)
        
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))


stime = time.time()
#print(2 == Solution().bulbSwitch(4))
#print(2 == Solution().bulbSwitch(5))
print(2 == Solution().bulbSwitch(6))
print('elapse time: {} sec'.format(time.time() - stime))