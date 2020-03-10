
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def generateTheString(self, n: int) -> str:
        odd = even = n
        
        if n%2 != 0:
            return 'a'*n
        
        def dfs(n, ch):
            res = ''
            odd1 = odd2 = 0
            if n%2 == 0:
                odd1, odd2 = n - 1, 1
            else:
                even = n//2 + 1
                odd = n - even
                res = dfs(even, chr(ord(ch) + 3))
                res += odd*chr(ord(ch) + 2)
            
            return odd1*ch + odd2*chr(ord(ch) + 1) + res
    
        return dfs(n, 'a')
        
            
            
stime = time.time()
print("holasss" == Solution().generateTheString(n = 7))
print('elapse time: {} sec'.format(time.time() - stime))