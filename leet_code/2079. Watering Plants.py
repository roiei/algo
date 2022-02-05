import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        seq = []
        inc = 0
        for val in plants:
            inc += val
            seq += inc,
        
        num = capacity
        cnt = 0
        print(seq)
        while True:
            idx = bisect.bisect_left(seq, num)
            print(num, idx)
            if idx >= len(seq):
                cnt += idx
                print(cnt)
                break
            
            cnt += idx*2
            print(cnt)
            
            diff = seq[idx] - num
            num += capacity - diff
        
        return cnt

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        seq = [capacity]
        
        for val in plants:
            if seq[-1] < val:
                seq[-1] = capacity
            
            seq += seq[-1] - val,
    
        cnt = 0
        for i, val in enumerate(seq):
            if val == capacity:
                if i != len(seq) - 1:
                    cnt += i*2
                else:
                    cnt += i
            else:
                if i == len(seq) - 1:
                    cnt += i
        
        return cnt


stime = time.time()
print(14 == Solution().wateringPlants(plants = [2,2,3,3], capacity = 5))
print(30 == Solution().wateringPlants(plants = [1,1,1,4,2,3], capacity = 4))
print('elapse time: {} sec'.format(time.time() - stime))
