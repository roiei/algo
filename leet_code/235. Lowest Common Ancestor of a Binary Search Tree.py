import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target, trace, out):
            trace += node.val,            
            if node.val == target:
                out += trace[::-1]
                trace.pop()
                return
            if node.left == None and node.right == None:
                trace.pop()
                return None
            if None != node.left:
                dfs(node.left, target, trace, out)
            if None != node.right:
                dfs(node.right, target, trace, out)
            trace.pop()
        
        ptrace, qtrace = [], []
        dfs(root, p.val, [], ptrace)
        dfs(root, q.val, [], qtrace)
        
        def find_val(src, ss):
            m = len(src)
            n = len(ss)
            i = m-1
            j = n-1
            cnt = 0
            while i >= 0 and j >= 0:
                if src[i] != ss[j]:
                    break
                i -= 1
                j -= 1
                cnt += 1
            if 0 != cnt:
                return m-cnt
            return -1
    
        lca = -1
        idx = find_val(ptrace, qtrace)
        if -1 != idx:
            lca = ptrace[idx]
        return TreeNode(lca)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            nonlocal common
            if not node:
                return set()

            res = set(dfs(node.left) | dfs(node.right))

            if node.val == p.val or node.val == q.val:
                res.add(node.val)
                
            if len(res) == 2 and not common:
                common = node.val

            return res

        common = None
        dfs(root)
        return TreeNode(common)

            
stime = time.time()
print(TreeNode(6) == Solution().lowestCommonAncestor(deserialize('[6,2,8,0,4,7,9,null,null,3,5]'), TreeNode(0), TreeNode(8)))
#print(TreeNode(6) == Solution().lowestCommonAncestor(deserialize('[6,2,8,0,4,7,9,null,null,3,5]'), TreeNode(2), TreeNode(8))) # 6
#print(TreeNode(3) == Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(1))) # 3
#print(TreeNode(5) == Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(4))) # 5
#print(TreeNode(1) == Solution().lowestCommonAncestor(deserialize('[1,2,3,null,4]'), TreeNode(4), TreeNode(3))) # 1
print('elapse time: {} sec'.format(time.time() - stime))