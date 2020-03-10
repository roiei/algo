
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestConsecutive2(self, root):
        g = collections.defaultdict(dict)
        mn = float('inf')
        
        def dfs(node):
            nonlocal mn 
            if not node:
                return
            
            mn = min(mn, node.val)
            if node.left:
                g[node.val][node.left.val] = True
                g[node.left.val][node.val] = True
                dfs(node.left)
            
            if node.right:
                g[node.val][node.right.val] = True
                g[node.right.val][node.val] = True
                dfs(node.right)
            
        dfs(root)
        
        mx = 0
        q = [(mn, 1, 0)]
        visited = set()
        visited.add(mn)

        while q:
            node, length, sign = q.pop(0)
            mx = max(mx, length)
            
            for adj, linked in g[node].items():
                if adj in visited:
                    continue
                
                if adj > node and adj == node + 1:
                    if sign == 1 or sign == 0:
                        length += 1
                    else:
                        length = 1
                        sign = 1                
                elif adj < node and adj + 1 == node:
                    if sign == -1 or sign == 0:
                        length += 1
                    else:
                        length = 1
                        sign = -1
                else: # diff is more than 1
                    sign = 0
                    length = 1
                    
                visited.add(adj)
                q += (adj, length, sign),
            
        return mx

    def longestConsecutive2(self, root):
        def dfs(node, par_val):
            if not node:
                return 0, 0, 0  # max len, pos len, neg len
            
            l_max, l_pos, l_neg = dfs(node.left, node.val)
            r_max, r_pos, r_neg = dfs(node.right, node.val)
            
            pos = neg = 0
            
            if node.val == par_val + 1:
                pos = max(l_pos, r_pos) + 1
            elif node.val + 1 == par_val:
                neg = max(l_neg, r_neg) + 1
            
            mx = max(l_max, r_max, l_pos + r_neg + 1, l_neg + r_pos + 1)
            return mx, pos, neg
        
        mx, pos, neg = dfs(root, root.val)
        return mx







stime = time.time()
print(4 == Solution().longestConsecutive2(deserialize('[1,2,0,3]')))
# print(2 == Solution().longestConsecutive2(deserialize('[3,2,2]')))
# print(2 == Solution().longestConsecutive2(deserialize('[1,2,-5,4,null,5,6]')))
#print(5 == Solution().longestConsecutive2(deserialize('[1,2,null,3,null,1,null,2,null,3,null,4,null,5]')))
print('elapse time: {} sec'.format(time.time() - stime))