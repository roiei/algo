
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def pathInZigZagTree(self, label: int) -> [int]:
        n = 1
        seq = [1]
        toggle = True
        seed = 2
        
        while 2**n < label + 1:
            cnt = seed
            
            new = []
            for i in range(2**n):
                new += cnt,
                cnt += 1

            seed = new[-1] + 1
            
            if toggle:
                seq += new[::-1]
            else:
                seq += new

            toggle = not toggle
            n += 1

        res = []
        idx = seq.index(label)
        res += seq[idx],
        
        
        while idx:
            idx = (idx - 1)//2
            res += seq[idx],

        return res[::-1]


stime = time.time()
print(Solution().pathInZigZagTree(label = 16))
# print([1,3,4,14] == Solution().pathInZigZagTree(label = 14))
# print([1,2,6,10,26] == Solution().pathInZigZagTree(label = 26))
print('elapse time: {} sec'.format(time.time() - stime))