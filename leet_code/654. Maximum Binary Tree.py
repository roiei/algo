import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def dfs(node, left, right):
            if not nums:
                return
            if left:
                mx = max(left)
                idx = left.index(mx)
                node.left = TreeNode(mx)
                dfs(node.left, left[:idx], left[idx+1:])
            if right:
                mx = max(right)
                idx = right.index(mx)
                node.right = TreeNode(mx)
                dfs(node.right, right[:idx], right[idx+1:])                           
            
        root = TreeNode(max(nums))
        idx = nums.index(root.val)
        dfs(root, nums[:idx], nums[idx+1:])
        return root


stime = time.time()
print(Solution().constructMaximumBinaryTree([3,2,1,6,0,5]))
print('elapse time: {} sec'.format(time.time() - stime))