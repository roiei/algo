import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: int) -> TreeNode:
        q = [root]

        while q:
            nq = []
            line = []

            while q:
                node = q.pop(0)
                if node.left:
                    nq += node.left,
                if node.right:
                    nq += node.right,

                line += node,

            q = nq

            for i in range(len(line) - 1):
                if line[i].val == u and i + 1 < len(line):
                    return line[i + 1]

        return None


stime = time.time()
print(None == Solution().findNearestRightNode(deserialize('[3,null,4,2]'), 2))
print(TreeNode(5) == Solution().findNearestRightNode(deserialize('[1,2,3,null,4,5,6]'), 4))
print('elapse time: {} sec'.format(time.time() - stime))
