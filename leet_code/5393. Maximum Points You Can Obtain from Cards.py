
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:
        stk = [(0, len(cardPoints) - 1, 0, k)]
        mx = 0
        
        while stk:
            l, r, t, k = stk.pop(0)
            mx = max(mx, t)
            if l > r:
                continue
            if not k:
                continue

            stk += (l + 1, r, t + cardPoints[l], k - 1),
            stk += (l, r - 1, t + cardPoints[r], k - 1),
        
        return mx


    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def dfs(l, r, k):
            if (l, r) in mem:
                return mem[(l, r)]
            
            if not k:
                return 0
        
            if l > r:
                return 0
        
            mem[(l, r)] = max(dfs(l + 1, r, k - 1) + cardPoints[l], 
                dfs(l, r - 1, k - 1) + cardPoints[r])
            return mem[(l, r)]
    
        mem = {}
        return dfs(0, len(cardPoints) - 1, k)


    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints) - k
        mnleft = left = sum(cardPoints[:length])
        
        for i in range(length, len(cardPoints)):
            left += cardPoints[i]
            left -= cardPoints[i - length]
            mnleft = min(mnleft, left)
        
        return sum(cardPoints) - mnleft



stime = time.time()
print(12 == Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))