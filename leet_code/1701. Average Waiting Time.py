import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ends = []
        for arr, time in customers:
            if not ends:
                ends += arr + time,
                continue
            
            gap = ends[-1] - arr
            if gap > 0:
                arr += gap
            
            ends += arr + time,
        
        wait_times = []
        for customer, end in zip(customers, ends):
            arr, time = customer
            wait_times += end - arr,
        
        return sum(wait_times)/len(wait_times)


stime = time.time()
print(5.00000 == Solution().averageWaitingTime(customers = [[1,2],[2,5],[4,3]]))
print('elapse time: {} sec'.format(time.time() - stime))