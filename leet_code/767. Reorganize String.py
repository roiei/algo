
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = collections.Counter(S)
        res = []
        most_common_char, count = freq.most_common(1)[0]
        
        if count > (len(S) + 1)/2:
            return ""
        
        while freq:
            next_most_common_chars = freq.most_common(2)        # 1st, 2nd
            chrs = [ch for ch, cnt in next_most_common_chars]
            res += chrs

            for ch in chrs:
                freq[ch] -= 1
                if freq[ch] == 0:
                    del freq[ch]
            
        return "".join(res)


    def reorganizeString(self, S: str) -> str:
        freq = collections.Counter(S)
        res = []
        freq = sorted(freq.items(), key=lambda p: p[1])
        freq = [[k, v] for k, v in freq]
        
        if freq[-1][1] > (len(S) + 1)/2:
            return ""

        def biesct_left(seq, val):
            l = 0
            r = len(seq) - 1
            while l <= r:
                m = (l + r)//2
                if seq[m][1] == val:
                    return m
                if seq[m][1] > val:
                    r = m - 1
                else:
                    l = m + 1
            return l

        while freq:
            first = freq.pop()
            second = None
            if freq:
                second = freq.pop()

            res += first[0],
            if second:
                res += second[0],

            first[1] -= 1
            if second:
                second[1] -= 1

            if first[1] > 0:
                idx = biesct_left(freq, first[1])
                freq.insert(idx, first)

            if second and second[1] > 0:
                idx = biesct_left(freq, second[1])
                freq.insert(idx, second)

        return "".join(res)
                

stime = time.time()
#print("aba" == Solution().reorganizeString("aab"))
#print("" == Solution().reorganizeString("aaab"))
print("vlvov" == Solution().reorganizeString("vvvlo"))
print('elapse time: {} sec'.format(time.time() - stime))

