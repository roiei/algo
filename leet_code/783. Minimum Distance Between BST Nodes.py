import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def minDiffInBST(self, root: 'TreeNode') -> int:
        q = [root]
        values = []

        while q:
            cur = q.pop(0)
            values.append(cur.val)

            if None != cur.left:
                q.append(cur.left)

            if None != cur.right:
                q.append(cur.right)

        mn = float('inf')
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                mn = min(mn, abs(values[i] - values[j]))
        
        return mn

    def minDiffInBST(self, root: 'TreeNode') -> int:
        def dfs(node):
            if not node.left and not node.right:
                return [node.val]

            l, r = [], []

            if node.left:
                l += dfs(node.left)

            if node.right:
                r += dfs(node.right)

            return l + [node.val] + r

        nums = dfs(root)
        mn = float('inf')
        for i in range(1, len(nums)):
            mn = min(mn, nums[i] - nums[i - 1])

        return mn


stime = time.time()
print(1 == Solution().minDiffInBST(deserialize('[4,2,6,1,3,null,null]')))
print(6 == Solution().minDiffInBST(deserialize('[27,null,34,null,58,50,null,44,null,null,null]')))
print('elapse time: {} sec'.format(time.time() - stime))
