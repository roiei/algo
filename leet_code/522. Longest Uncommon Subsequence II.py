import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def findLUSlength(self, strs):
        def subseq(substr, srcstr):
            i = 0
            n = len(substr)
            for ch in srcstr:
                if i < n and substr[i] == ch:
                    i += 1
            return i == len(substr)
            
        strs.sort(key=len, reverse=True)

        for i, substr in enumerate(strs):
            no_all_subsequence = True
            for j, srcstr in enumerate(strs):
                if i == j or len(srcstr) < len(substr):
                    continue
                if True == subseq(substr, srcstr):
                    no_all_subsequence = False
                    break
                    
            if True == no_all_subsequence: # mean this stubstr is longest and no sub
                return len(substr)
        return -1

            

            

stime = time.time()
print(2 == Solution().findLUSlength(["aabbcc", "aabbcc","cb","abc"]))
#print(Solution().findLUSlength(["aaa","aaa","aa"]))
print('elapse time: {} sec'.format(time.time() - stime))