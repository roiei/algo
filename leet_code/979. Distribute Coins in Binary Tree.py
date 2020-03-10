import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def distributeCoins(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0, 0     # my coin, child's movement

            l_coin, l_mv = dfs(node.left)
            r_coin, r_mv = dfs(node.right)

            coin = node.val - 1 + l_coin + r_coin
            mv = abs(l_coin) + abs(r_coin) + l_mv + r_mv
            return coin, mv

        return dfs(root)[-1]


stime = time.time()
print(1 == Solution().distributeCoins(deserialize('[2,1,0]')))
print(2 == Solution().distributeCoins(deserialize('[3,0,0]')))
print(3 == Solution().distributeCoins(deserialize('[0,3,0]')))
print(2 == Solution().distributeCoins(deserialize('[1,0,2]')))
print(4 == Solution().distributeCoins(deserialize('[1,0,0,null,3]')))
print(6 == Solution().distributeCoins(deserialize('[4, 0, null, null, 0, null, 0]')))
print('elapse time: {} sec'.format(time.time() - stime))