import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def partitionLabels(self, S: str) -> [int]:
        ch_idxs = collections.defaultdict(list)
        idx_chs = collections.defaultdict(lambda: set())
        for i, ch in enumerate(S):
            ch_idxs[ch] += i,
            idx_chs[i].add(ch)
        
        pre_chs = idx_chs[0]
        
        for idx, chs in idx_chs.items():
            idx_chs[idx] |= pre_chs
            pre_chs = idx_chs[idx]
        
        i = 0
        res = []

        while i < len(S):
            ch = S[i]
            last_idx = ch_idxs[ch][-1]
            included_chs = idx_chs[last_idx]

            mx = 0
            for ch in included_chs:
                mx = max(mx, ch_idxs[ch][-1])

            while mx > last_idx:
                last_idx = mx

                included_chs = idx_chs[last_idx]
                for ch in included_chs:
                    mx = max(mx, ch_idxs[ch][-1])

            res += mx - i + 1,
            i = mx + 1
    
        return res


#  0       8    9      15  16     23
# "ababcbaca", "defegde", "hijhklij".


# 0
# qiejxqfnqceoc m y
# 
# qiejxqfnqce oc m y

stime = time.time()
#print([9,7,8] == Solution().partitionLabels(S = "ababcbacadefegdehijhklij"))
print([13,1,1] == Solution().partitionLabels(S = "qiejxqfnqceocmy"))
print('elapse time: {} sec'.format(time.time() - stime))

