
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        used = []
        adict = {}
        
        for i, ch in enumerate(s):
            if ch not in adict and t[i] not in used:
                adict[ch] = t[i]
                used += t[i],
            
            if ch not in adict or adict[ch] != t[i]:
                return False
        
        return True


stime = time.time()
print(True == Solution().convert("egg", "add"))
print(False == Solution().convert("foo", "bar"))
print(True == Solution().convert("paper", "title"))
print('elapse time: {} sec'.format(time.time() - stime))