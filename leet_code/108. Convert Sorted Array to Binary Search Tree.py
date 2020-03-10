import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        def dfs(nums, l, r):
            if l > r:
                return None
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = dfs(nums, l, m-1)
            node.right = dfs(nums, m+1, r)
            return node
    
        return dfs(nums, 0, len(nums)-1)
            

stime = time.time()
print('1a' == Solution().sortedArrayToBST([-10,-3,0,5,9]))
print('elapse time: {} sec'.format(time.time() - stime))