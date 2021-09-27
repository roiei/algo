import time
import collections


class Solution:
    def validTree(self, n, edges):
        root = [i for i in range(n)]

        for src, sink in edges:
            root1 = self.findRoot(root, src)
            root2 = self.findRoot(root, sink)
            if root1 == root2:
                return False
            else:
                root[root2] = root1

        return len(edges) == n - 1

    def findRoot(self, root, node):
        if root[node] == node:
            return node
        else:
            return self.findRoot(root, root[node])

    def validTree(self, n, edges):
        parents = collections.defaultdict(int)
        for src, dst in edges:
            parents[src] = src
            parents[dst] = dst
        
        def find_parent(parents, idx):
            while parents[idx] != idx:
                idx = parents[idx]
            return idx

        for src, sink in edges:
            src_parent = find_parent(parents, src)
            dst_parent = find_parent(parents, sink)
            if src_parent == dst_parent:
                return False
            
            parents[dst_parent] = src_parent

        return len(edges) == n - 1

    def validTree(self, n, edges):
        def is_exist(u, v):
            visited = set()
            visited.add(u)
            q = [u]

            while q:
                cur = q.pop(0)

                if cur == v:
                    return True

                for adj in g[u]:
                    if adj in visited:
                        continue

                    q += adj,
                    visited.add(adj)

            return False

        g = collections.defaultdict(list)
        for u, v in edges:
            if is_exist(u, v):
                return False

            g[u] += v,
            g[v] += u,

        return len(edges) == n - 1


stime = time.time()
#print(True == Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(False == Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(False == Solution().validTree(10, [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]))



print('elapse time: {} sec'.format(time.time() - stime))