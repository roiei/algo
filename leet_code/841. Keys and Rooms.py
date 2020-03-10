
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = collections.defaultdict(dict)
        
        for i, room in enumerate(rooms):
            for num in room:
                g[i][num] = True
            
        q = [0]
        visited = set()
        visited.add(0)
        
        while q:
            u = q.pop(0)
            
            for adj, link in g[u].items():
                if adj in visited:
                    continue
                
                q += adj,
                visited.add(adj)
        
        return len(rooms) == len(visited)


stime = time.time()
print(False == Solution().canVisitAllRooms([[1],[],[0,3],[1]]))
print(True == Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(False == Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print('elapse time: {} sec'.format(time.time() - stime))