import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, nodes):
            if not node:
                return

            dfs(node.right, nodes)
            nodes += node,
            dfs(node.left, nodes)

        nodes = []
        dfs(root, nodes)

        inc = 0
        for node in nodes:
            inc += node.val
            node.val = inc

        return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, weight):
            if not node:
                return

            dfs(node.right, weight)
            weight[0] += node.val
            node.val = weight[0]
            dfs(node.left, weight)

        weight = [0]
        dfs(root, weight)

        return root
        

stime = time.time()
print(traverse_level(deserialize('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')) == traverse_level(Solution().bstToGst(deserialize('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'))))
print('elapse time: {} sec'.format(time.time() - stime))