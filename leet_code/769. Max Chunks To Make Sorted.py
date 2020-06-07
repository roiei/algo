
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        def search(seq, num : 'end index'):
            l = 0
            r = len(seq) - 1
            
            while l <= r:
                m = (l + r)//2
                if seq[m][1] == num:
                    return m
                if num < seq[m][1]:
                    r = m - 1
                else:
                    l = m + 1
                
            return l
            
        seq = []
        
        for num in arr:
            idx = search(seq, num)
            seq.insert(idx, [num, num])
            
            while idx + 1 < len(seq):
                seq[idx][0] = min(seq[idx][0], seq[idx + 1][0])
                seq[idx][1] = max(seq[idx][1], seq[idx + 1][1])
                seq.pop(idx + 1)
        
        return len(seq)
        

stime = time.time()
print(1 == Solution().maxChunksToSorted([4,3,2,1,0]))
print(4 == Solution().maxChunksToSorted([1,0,2,3,4]))
print(2 == Solution().maxChunksToSorted([1,2,0,3]))
print(1 == Solution().maxChunksToSorted([2,0,1]))
print('elapse time: {} sec'.format(time.time() - stime))