
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def buildArray(self, target: [int], n: int) -> [str]:
        idx = 0
        val = 0
        seq = []
        res = []
        
        for num in range(1, n + 1):
            if idx >= len(target):
                break
                
            seq += num,
            res += 'Push',

            if seq[-1] == target[idx]:
                idx += 1
            elif seq:
                seq.pop()
                res += 'Pop',
        
        return res
                

stime = time.time()
print(["Push","Push","Pop","Push"] == Solution().buildArray(target = [1,3], n = 3))
print('elapse time: {} sec'.format(time.time() - stime))