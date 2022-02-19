
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def getMinCostforCoorinates(self, coordinates: List[List[int]]) -> int:
        links = []

        n = len(coordinates)
        for i in range(n - 1):
            for j in range(i + 1, n):
                w = abs(coordinates[i][0] - coordinates[j][0]) + \
                    abs(coordinates[i][1] - coordinates[j][1])
                links += (i, j, w),
    
        links.sort(key=lambda p: p[2])
        
        union = [i for i in range(n)]
        
        def find_root(key):
            while union[key] != key:
                key = union[key]
            return key
        
        cost = 0
        cnt = 0

        while links and cnt < n - 1:
            u, v, w = links.pop(0)
            uroot = find_root(u)
            vroot = find_root(v)
            
            if uroot != vroot:
                union[vroot] = uroot
                cost += w
                cnt += 1
        
        return cost

    def minCostConnectPoints(self, coordinates: List[List[int]]) -> int:
        links = []
        union = collections.defaultdict(None)
        vertices = set()

        n = len(coordinates)
        for i in range(n - 1):
            for j in range(i + 1, n):
                u = '{},{}'.format(coordinates[i][0], coordinates[i][1])
                v = '{},{}'.format(coordinates[j][0], coordinates[j][1])
                w = abs(coordinates[i][0] - coordinates[j][0]) + \
                    abs(coordinates[i][1] - coordinates[j][1])
                links += (u, v, w),
                vertices.add(u)
                vertices.add(v)
    
        links = collections.deque(sorted(links, key=lambda p: p[2]))
        print(links)
        
        for vertice in vertices:
            union[vertice] = vertice
        
        def find_root(key):
            while union[key] != key:
                key = union[key]
            return key
        
        cost = 0
        cnt = 0

        while links and cnt < n - 1:
            u, v, w = links.popleft()
            uroot = find_root(u)
            vroot = find_root(v)
            
            if uroot != vroot:
                print(u, v, w)
                union[vroot] = uroot
                cost += w
                cnt += 1
        
        return cost


stime = time.time()
#print(20 == Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(19 == Solution().minCostConnectPoints(coordinates = [[0,0],[3,3],[4,9],[6,4],[7,3]]))
print('elapse time: {} sec'.format(time.time() - stime))
