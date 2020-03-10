import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def distanceK(self, root, target, K):
        if not root:
            return []
        
        def dfs(node, par, link):
            if None == node:
                return
            link += (node.val, par.val),
            dfs(node.left, node, link) 
            dfs(node.right, node, link)
        
        link = []
        dfs(root.left, root, link)
        dfs(root.right, root, link)
        if not link:
            return []
        n = max(link)[0]+1
        g = [[0]*n for _ in range(n)]
        for l in link:
            g[l[0]][l[1]] = 1
            g[l[1]][l[0]] = 1
        
        res = []
        visit = [False]*n
        q = [(target.val, 0)]
        while q:
            cur, depth = q.pop(0)
            if K == depth:
                res += cur,
            visit[cur] = True
            for i in range(len(g[cur])):
                if 1 == g[cur][i] and False == visit[i]:
                    q += (i, depth+1),
        return res


stime = time.time()
print(Solution().distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 2))
print('elapse time: {} sec'.format(time.time() - stime))