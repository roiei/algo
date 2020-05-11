
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def get_chunks(s):
            if not s:
                return
            
            pre = s[0]
            cnt = 1
            chunks = []
            
            for i in range(1, len(s)):
                if s[i] == pre:
                    cnt += 1
                else:
                    chunks += (pre, cnt),
                    pre = s[i]
                    cnt = 1
            
            chunks += (pre, cnt),
            
            return chunks
    
        chunks = get_chunks(name)
        
        i = 0
        for ch, cnt in chunks:
            while cnt and i < len(typed) and typed[i] == ch:
                i += 1
                cnt -= 1

            while i < len(typed) and typed[i] == ch:
                i += 1
            
            if cnt:
                return False

        return i == len(typed)
        

stime = time.time()
print(True == Solution().isLongPressedName(name = "alex", typed = "aaleex"))
print(False == Solution().isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(True == Solution().isLongPressedName(name = "leelee", typed = "lleeelee"))
print(True == Solution().isLongPressedName(name = "laiden", typed = "laiden"))
print(False == Solution().isLongPressedName("pyplrz", "ppyypllr"))
print(False == Solution().isLongPressedName("alex", "alexxr"))
print('elapse time: {} sec'.format(time.time() - stime))