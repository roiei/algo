
import time
#from util.util_list import *
#from util.util_tree import *
import copy
import collections


class Solution(object):
    def getShortestLenAlphabet(self, s:str) -> int:
        
        idxs = []
        for i, ch in enumerate(s):
            if ch == 'a' or ch == 'c':
                idxs += (ch, i),
        
        idxs = sorted(idxs, key=lambda p:p[1], reverse=False)
        n = len(idxs)
        mn = float('inf')


        def check_completeness(s, l, r):
            ch = 'a'
            while l <= r:
                if s[l] == ch:
                    ch = chr(ord(ch) + 1)
                if ch == 'c':
                    break
                l += 1
            return ch == 'c'

        i = 0
        while i < n:
            while i < n and idxs[i][0] != 'a':
                i += 1
            si = idxs[i][1]

            if i == n:
                break

            while i < n and idxs[i][0] != 'c':
                i += 1

            if i == n:
                break

            ei = idxs[i][1]

            if False == check_completeness(s, si, ei):
                continue

            mn = min(mn, ei - si)
            i += 1

        return mn



stime = time.time()
print(Solution().getShortestLenAlphabet('0c00a0b0c000c00a0b00c0a0'))
print('elapse time: {} sec'.format(time.time() - stime))