import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def shortestToChar(self, S: str, C: str) -> [int]:
        coords = []
        for i, ch in enumerate(S):
            if ch == C:
                coords += i,
        
        dist = [float('inf')]*len(S)
        for coord in coords:
            for i, ch in enumerate(S):
                dist[i] = min(dist[i], abs(coord-i))
        return dist

    def shortestToChar(self, S, C):
        n = len(S)
        c_pos = float('inf')
        out = [float('inf')]*n
        
        for i in range(n):
            if S[i] == C:
                c_pos = 0
            out[i] = min(out[i], c_pos)
            c_pos += 1
        
        c_pos = float('inf')
        for i in range(n-1, -1, -1):
            if S[i] == C:
                c_pos = 0
            out[i] = min(out[i], c_pos)
            c_pos += 1
        return out
            

stime = time.time()
print([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0] == Solution().shortestToChar("loveleetcode", 'e'))
print('elapse time: {} sec'.format(time.time() - stime))