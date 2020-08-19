
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def find_deepest(node):
            q = [node]
            lev = []

            while q:
                nq = []
                seq = []

                while q:
                    node = q.pop(0)
                    seq += node,
                    if node.left:
                        nq += node.left,
                    if node.right:
                        nq += node.right,
                q = nq
                lev = seq
            return lev

        deepest_nodes = find_deepest(root)
        print(deepest_nodes)
        
        def dfs(node, lev):
            if not node:
                return False

            if not node.left and not node.right and node in deepest_nodes:
                ancestors[lev] = node
                return True

            if node in deepest_nodes:
                return True

            lr = dfs(node.left, lev + 1)
            rr = dfs(node.right, lev + 1)

            if lr and rr:
                ancestors[lev] = node

            return lr or rr

        ancestors = collections.defaultdict(None)
        dfs(root, 0)
        ancestors = sorted(ancestors.items(), key=lambda p: p[0], reverse=False)

        print(ancestors)        
        return ancestors[0][1]


stime = time.time()
#print(tree_is_same(deserialize('[1,2,3]'), Solution().lcaDeepestLeaves(deserialize('[1,2,3]'))))
print(tree_is_same(deserialize('[4]'), Solution().lcaDeepestLeaves(deserialize('[1,2,3,4]'))))
print('elapse time: {} sec'.format(time.time() - stime))

