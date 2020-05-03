
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        n = len(s)
        
        wnd = []
        for ch in s:
            if ch in wnd:
                while wnd and wnd[0] != ch:
                    wnd.pop(0)
                wnd.pop(0)
            wnd += ch,
            mlen = max(mlen,  len(wnd))
            
        return mlen

    def lengthOfLongestSubstring(self, s: str) -> int:
        idxs = collections.defaultdict(int)
        vals = []
        idx = 0
        mx = 0
        
        for ch in s:
            if ch in vals:
                pre = len(vals)
                vals = vals[idxs[ch] + 1:]
                idx = len(vals)
                offset = pre - idx
                for k in idxs:
                    idxs[k] -= offset
                
            vals += ch,
            idxs[ch] = idx
            idx += 1
            mx = max(mx, len(vals))
        
        return mx


print(7 == Solution().lengthOfLongestSubstring("bpfbhmipx"))