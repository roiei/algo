
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None

            if node.left:
                node.left = dfs(node.left)

            if node.right:
                node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)
       

stime = time.time()
res = Solution().removeLeafNodes(deserialize('[1,2,3,2,null,2,4]'), target = 2)
print(traverse_level(deserialize('[1,null,3,null,4]')) == traverse_level(res))
print('elapse time: {} sec'.format(time.time() - stime))