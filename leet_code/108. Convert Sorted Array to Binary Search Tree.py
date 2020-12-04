import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
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

    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        
        def dfs(l, r):
            if l > r:
                return None
            
            m = (l + r)//2
            node = TreeNode(nums[m])
            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)
            return node
    
        return dfs(0, len(nums) - 1)
            

stime = time.time()
print(traverse_level(deserialize('[0,-10,5,-3,9]')))
print(traverse_level(Solution().sortedArrayToBST([-10,-3,0,5,9])))
print(tree_is_same(deserialize('[0,-10,5,-3,9]'), ))
print('elapse time: {} sec'.format(time.time() - stime))