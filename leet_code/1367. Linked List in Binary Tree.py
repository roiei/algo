
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        seq = ''
        while head:
            seq += str(head.val)
            head = head.next

        def dfs(node, trace):
            if not node:
                return True if seq in trace else False

            lr = dfs(node.left, trace + str(node.val))
            rr = dfs(node.right, trace + str(node.val))
            return lr or rr

        return dfs(root, '')



stime = time.time()
print(True == Solution().isSubPath(create_linked_list_from_nums([4,2,8]), deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')))
print(True == Solution().isSubPath(create_linked_list_from_nums([1,4,2,6]), deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')))
print(False == Solution().isSubPath(create_linked_list_from_nums([1,4,2,6,8]), deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')))
print('elapse time: {} sec'.format(time.time() - stime))