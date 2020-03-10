import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def verticalTraversal(self, root: TreeNode) -> [[int]]:
        vert = collections.defaultdict(lambda : collections.defaultdict(list))

        def dfs(node, vert, y, x):
            vert[x][y] += node.val,
            if node.left:
                dfs(node.left, vert, y+1, x-1)
            if node.right:
                dfs(node.right, vert, y+1, x+1)

        dfs(root, vert, 0, 0)

        kv = sorted(vert.items(), key=lambda p:p[0], reverse=False)
        out = []
        for x, line in kv:
            t = []
            for y, li in sorted(line.items()):
                t += sorted(li)
            out += t,
        return out
            

stime = time.time()
print(Solution().verticalTraversal(deserialize('[3,9,20,null,null,15,7]')))
print('elapse time: {} sec'.format(time.time() - stime))