import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def rob(self, root: TreeNode) -> int:
        dp = {}
        if not root:
            return 0
        def dfs(node):
            if None == node:
                return 0
            if node in dp:
                return dp[node]
            cur_val = node.val
            if None != node.left:
                cur_val += dfs(node.left.left) + dfs(node.left.right)
            if None != node.right:
                cur_val += dfs(node.right.left) + dfs(node.right.right)
            sub_val = dfs(node.left) + dfs(node.right)
            dp[node] = max(cur_val, sub_val)
            return dp[node]
        return dfs(root)


stime = time.time()
print(Solution().rob(deserialize('[3,4,7,1,3,null,1,2,7,null,3]')))
#print(Solution().rob(deserialize('[3,2,3,null,3,null,1]')))
#print(Solution().rob(deserialize('[4,1,null,2,null,3]')))
print('elapse time: {} sec'.format(time.time() - stime))