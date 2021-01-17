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
        return TreeNode(lca).val


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        
        def dfs(node):
            nonlocal res

            ret = False
            if not node:
                return ret
            
            if node.val == p.val or node.val == q.val:
                ret = True
            
            lr = dfs(node.left)
            rr = dfs(node.right)

            if (((lr or ret) and rr) or (lr and (rr or ret))) and not res:
                res = node
            
            ret = ret or lr or rr
            return ret
        
        dfs(root)
        return res.val

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            nonlocal common

            if not node:
                return None
        
            ret = False
            if node == p or node == q:
                ret = True
                print('True')
                
            lr = dfs(node.left)
            rr = dfs(node.right)

            if ((lr or ret) and rr) or (lr and (rr or ret)) and not common:
                common = node
        
            ret = ret or lr or rr
            return ret
    
        common = None
        dfs(root)
        return common.val if common else None
        

stime = time.time()
print(3 == Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(1))) # 3
print(5 == Solution().lowestCommonAncestor(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(4))) # 5
#print(Solution().lowestCommonAncestor(deserialize('[1,2,3,null,4]'), TreeNode(4), TreeNode(3))) # 1
#print(Solution().lowestCommonAncestor(deserialize('[-1,0,3,-2,4,null,null,8]'), TreeNode(8), TreeNode(4)))  # 0
print('elapse time: {} sec'.format(time.time() - stime))