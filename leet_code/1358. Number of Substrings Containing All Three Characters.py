
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pre_res = res = 0
        cnt = 0
        tot = 0
        
        aidx = bidx = cidx = 0
        bits = collections.defaultdict(int)
        bits['a'] = 1
        bits['b'] = 2
        bits['c'] = 4
        idxs = collections.defaultdict(int)
        
        for i, ch in enumerate(s):
            if ch in bits:
                cnt |= bits[ch]
                idxs[ch] = i

            if (ch in bits) and cnt == 7:
                tot += 1 + min(idxs.values())
                        
        return tot
            
            
stime = time.time()
print(10 == Solution().numberOfSubstrings("abcabc"))
print('elapse time: {} sec'.format(time.time() - stime))