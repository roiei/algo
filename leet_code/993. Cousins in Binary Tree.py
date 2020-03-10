import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        info = {}
        def dfs(node, pval, depth, x, y):
            if node.val == x or node.val == y:
                if node.val not in info:
                    info[node.val] = [pval, depth]
            if node.left == None and node.right == None:
                return
            if node.left != None:
                dfs(node.left, node.val, depth+1, x, y)
            if node.right != None:
                dfs(node.right, node.val, depth+1, x, y)
        
        dfs(root, -1, 1, x, y)
        if info[x][0] != info[y][0] and info[x][1] == info[y][1]:
            return True
        return False


stime = time.time()
print(Solution().isCousins(deserialize('[1,2,3,null,4,null,5]'), 5, 4))
print('elapse time: {} sec'.format(time.time() - stime))

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]