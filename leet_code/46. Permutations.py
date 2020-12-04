import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
    time complexity:
        permutation complexity = O(N!)
        cuz, ex. case 4, 4 x 3 x 2 x 1
            1
                2
                    3
                        4
                    4
                        3
                3
                    4
                        2
                    2
                        4
                4
                    2
                        3
                    3
                        2
            2
                1
                    3
                        4
                    4
                3
                    1
                        ...

"""

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def perm(selected, res, nums):
            if len(selected) == len(nums):
                res += selected[:],
                return
            for num in nums:
                if num in selected:
                    continue
                
                selected += num,
                perm(selected, res, nums)
                selected.pop(selected.index(num))
            
        res = []
        perm([], res, nums)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(seq, res):
            if len(seq) == len(nums):
                res += seq,
                return
        
            for num in nums:
                if num in seq:
                    continue
                
                dfs(seq + [num], res)
        
        res = []
        dfs([], res)
        return res
            


stime = time.time()
print(Solution().permute([1,2,3,4,5]))
print('elapse time: {} sec'.format(time.time() - stime))