import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> [int]:
        if not root:
            return []
        freq = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                freq[node.val] += 1
                return node.val
            val = node.val
            val += dfs(node.left)
            val += dfs(node.right)
            freq[val] += 1
            return val
        
        dfs(root)
        sfreq = sorted(freq.items(), key=lambda p:p[1], reverse=True)
        return [k for k,v in sfreq if v == sfreq[0][1]]


stime = time.time()
print([1,2] == Solution().findFrequentTreeSum(deserialize('[1,null,1]')))
print('elapse time: {} sec'.format(time.time() - stime))