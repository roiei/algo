import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        all_num = set([i for i in range(1, len(nums)+1)])
        return  list(all_num - uniq)


stime = time.time()
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))