
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = collections.Counter(s1)
        n = len(s1)
        f2 = collections.Counter(s2[:n])

        if f1 == f2:
            return True
        
        for i in range(n, len(s2)):
            f2[s2[i]] += 1
            f2[s2[i - n]] -= 1
            if f2[s2[i - n]] == 0:
                del f2[s2[i - n]]
            if f1 == f2:
                return True
    
        return False


stime = time.time()
print(True == Solution().checkInclusion("ab", "eidbaooo"))
print('elapse time: {} sec'.format(time.time() - stime))

