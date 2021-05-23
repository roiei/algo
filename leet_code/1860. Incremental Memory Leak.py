import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        tot = memory1 + memory2
        inc = 0
        i = 1
        crash_cnt = 1
        trace = []
        
        while inc + i <= tot:
            trace += i,
            inc += i
            i += 1

        for num in trace:
            if memory1 < memory2:
                if memory2 >= num:
                    memory2 -= num
                else:
                    break
            elif memory1 >= num:
                memory1 -= num
            else:
                break
            
            crash_cnt += 1
        
        return [crash_cnt, memory1, memory2]
        
            
stime = time.time()
print([3,1,0] == Solution().memLeak(memory1 = 2, memory2 = 2))
print([6,0,4] == Solution().memLeak(memory1 = 8, memory2 = 11))
print('elapse time: {} sec'.format(time.time() - stime))

     