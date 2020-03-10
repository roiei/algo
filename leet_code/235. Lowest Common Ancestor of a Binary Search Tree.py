import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


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
            

stime = time.time()
#print(Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(1))) # 3
print(Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(4))) # 5
#print(Solution().lowestCommonAncestor(deserialize('[1,2,3,null,4]'), TreeNode(4), TreeNode(3))) # 1
#print(Solution().lowestCommonAncestor(deserialize('[-1,0,3,-2,4,null,null,8]'), TreeNode(8), TreeNode(4)))  # 0
print('elapse time: {} sec'.format(time.time() - stime))