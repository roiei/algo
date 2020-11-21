
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def findClosestLeaf(self, root, k):
        g = collections.defaultdict(dict)
        leaves = collections.defaultdict(int)

        def dfs(node, g, par, is_sub):
            nonlocal leaves
            if not node:
                return

            if node.val == k:
                is_sub = True

            if not node.left and not node.right:
                if is_sub:
                    leaves[node.val] = 1
                else:
                    leaves[node.val] = 2

            if par:
                g[par][node.val] = True
                g[node.val][par] = True

            dfs(node.left, g, node.val, is_sub)
            dfs(node.right, g, node.val, is_sub)


        dfs(root, g, None, False)

        q = [(k, 0)]
        visited = set()
        visited.add(k)
        nums = collections.defaultdict(list)

        while q:
            node, depth = q.pop(0)
            if node in leaves:
                nums[node] = [depth, leaves[node]]

            for adj, linked in g[node].items():
                if adj in visited:
                    continue

                visited.add(adj)
                q += (adj, depth + 1),


        nums = sorted(nums.items(), key=lambda p: p[1][0])  #[1] is value, [0] is key
        min_dep = nums[0][1][0]
        nums = [(k, v[1]) for k, v in nums if v[0] == min_dep]
        nums.sort(key=lambda p: p[1])
        return nums[0][0]


stime = time.time()
#print(3 == Solution().findClosestLeaf(deserialize('[1, 3, 2]'), k = 1))
#print(12 == Solution().findClosestLeaf(deserialize('[10,12,13,null,null,14,15,21,22,23,24,1,2,3,4,5,6,7,8]'), k = 13))
print(10 == Solution().findClosestLeaf(deserialize('[1, 3, 4, null, null, null, 9, null, 10]'), k = 4))
print('elapse time: {} sec'.format(time.time() - stime))