import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def find_longest_sequence(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0, 0
            
            if not node.left and not node.right:
                return 1, 1
                
            llen, lmx = dfs(node.left)
            rlen, rmx = dfs(node.right)

            llen = llen + 1 if node.left and node.left.val == node.val + 1 else 1
            rlen = rlen + 1 if node.right and node.right.val == node.val + 1 else 1

            length = max(llen, rlen)
            return length, max(lmx, rmx, length)
        
        length, mx = dfs(root)
        return mx


#_, mx_length = find_longest_sequence(deserialize('[1,null,2,null,4,null,5,null,6]'))
#print(mx_length)


stime = time.time()
print(Solution().find_longest_sequence(deserialize('[1,null,4,5,5,6]')))
#print(3 == Solution().longestConsecutive(deserialize('[1,null,2,null,4,null,5,null,6]')))
#print(Solution().longestConsecutive(deserialize('[3,2,1]')))
#print(Solution().longestConsecutiveSequence(deserialize('[1,null,3,2,4,null,null,null,5]')))
#print(Solution().longestConsecutiveSequence(deserialize('[2,null,3,2,null,1,null]')))
print('elapse time: {} sec'.format(time.time() - stime))