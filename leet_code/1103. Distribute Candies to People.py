import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        ans = [0]*num_people
        
        idx = 0
        i = 1
        while candies > 0:
            num = candies if i > candies else i
            ans[idx] += num
            candies -= num
            
            i += 1
            idx = (idx + 1)%num_people
        
        return ans


stime = time.time()
print([1,2,3,1] == Solution().distributeCandies(7, 4))
print('elapse time: {} sec'.format(time.time() - stime))