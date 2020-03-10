import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        def get_seq(node):
            if not node:
                return [None]
            if not node.left and not node.right:
                return [node.val]
            res = [node.val]
            res += get_seq(node.left)
            res += get_seq(node.right)
            return res
        
        sub = get_seq(t)

        def chk(node, sub):
            if not node:
                return False, [None]
            if not node.left and not node.right:
                if sub == [node.val]:
                    return True, [node.val]
                return False, [node.val]
            
            seq = [node.val]
            rets = []

            ret, vals = chk(node.left, sub)
            rets += ret,
            seq += vals

            ret, vals = chk(node.right, sub)
            rets += ret,
            seq += vals
            if seq == sub:
                return True, seq
            rets += False,
            return any(rets), seq
        ret, seq = chk(s, sub)
        return ret


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def dfs(node):
            if not node:
                return [None]

            res = [node.val]
            res += dfs(node.left)
            res += dfs(node.right)
            return res

        sub_trace = ','
        full_trace = ','
        sub_trace += ''.join([str(val)+',' for val in dfs(t)])
        full_trace += ''.join([str(val)+',' for val in dfs(s)])
        return True if -1 != full_trace.find(sub_trace) else False


stime = time.time()
print(False == Solution().isSubtree(deserialize('[12]'), deserialize('[2]')))
print('elapse time: {} sec'.format(time.time() - stime))