
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def allPossibleFBT(self, N: int) -> [TreeNode]:
        
        dp = [[] for _ in range(N + 1)]
        dp[1] = [TreeNode(0)]
        
        for i in range(2, N + 1):
            res = []
            
            for j in range(1, i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        print(i, j, i - 1 - j)
                        root = TreeNode(0)
                        root.left, root.right = left, right
                        res.append(root)
            dp[i] = res
        print(len(dp[N]))
        return dp[N]

            
stime = time.time()
print(Solution().allPossibleFBT(7))
print('elapse time: {} sec'.format(time.time() - stime))