import time
from util.util_list import *
from util.util_tree import *
from typing import List
import copy
import collections


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return []
        
        def construct(nums, s, e):
            if s == e:
                return None
            
            node = TreeNode(nums[s])
            end = e
            for i in range(s+1, e):
                if nums[s] < nums[i]:
                    end = i
                    break
                
            node.left = construct(nums, s+1, end)
            node.right = construct(nums, end, e)
            return node
    
        root = construct(preorder, 0, len(preorder))
        return root


    def create_binary_search_tree(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return []
        
        def dfs(nums, l, r):
            if l > r:
                return None

            node = TreeNode(nums[l])
            idx = r

            for i in range(l + 1, r + 1):
                if nums[l] < nums[i]:
                    idx = i - 1
                    break
                    
            node.left = dfs(nums, l + 1, idx)
            node.right = dfs(nums, idx + 1, r)

            return node
        
        return dfs(preorder, 0, len(preorder) - 1)


#print(traverse_level(create_binary_search_tree([4, 2, 1, 3, 6, 5])))

stime = time.time()
print(traverse_level(Solution().bstFromPreorder([4, 2, 1, 3, 6, 5])))
#print(Solution().bstFromPreorder([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))