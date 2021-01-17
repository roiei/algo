
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        cnt = 0
        
        def dfs(node, seq):
            nonlocal cnt

            if not node.left and not node.right:
                seq += [node.val]

                freq = collections.Counter(seq)
                odd = 0
                for k, v in freq.items():
                    if v%2 != 0:
                        if odd > 0:
                            break
                        odd += 1
                else:
                    cnt += 1
                return
        
            if node.left:
                dfs(node.left, seq + [node.val])

            if node.right:
                dfs(node.right, seq + [node.val])
        
        dfs(root, [])
        return cnt
                


stime = time.time()
print(2 == Solution().pseudoPalindromicPaths(deserialize('[2,3,1,3,1,null,1]')))
print('elapse time: {} sec'.format(time.time() - stime))