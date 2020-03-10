
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mx = max(a, b, c)
        bits = 0
        
        while mx >= (1<<bits):
            bits += 1
            
        def pad_zeros(val):
            res = '{:b}'.format(val)
            res = (bits - len(res))*'0' + res
            return res
    
        a = pad_zeros(a)
        b = pad_zeros(b)
        c = pad_zeros(c)

        n = len(c)
        tot_flip = 0
        
        for i in range(n):
            ones = sum([1 if val == '1' else 0 for val in [a[i], b[i]]])
            
            flip = 0
            if '1' == c[i] and ones == 0:
                flip += 1
            elif '0' == c[i] and ones > 0:
                flip += ones
            
            tot_flip += flip
        
        return tot_flip

    def minFlips(self, a: int, b: int, c: int) -> int:
        mx = max(a, b, c)
        bits = 0
        
        while mx >= (1<<bits):
            bits += 1
            
        def pad_zeros(val):
            res = '{:b}'.format(val)
            res = (bits - len(res))*'0' + res
            res = [val for val in list(map(int, res))]
            return res
    
        c = pad_zeros(c)
        vals = list(zip(pad_zeros(a), pad_zeros(b)))

        n = len(c)
        tot_flip = 0
        
        for i in range(n):
            ones = vals[i].count(1)
            
            flip = 0
            if 1 == c[i] and ones == 0:
                flip += 1
            elif 0 == c[i] and ones > 0:
                flip += ones
            
            tot_flip += flip
        
        return tot_flip

            
stime = time.time()
print(3 == Solution().minFlips(a = 2, b = 6, c = 5))
print('elapse time: {} sec'.format(time.time() - stime))