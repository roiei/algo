import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    """
    @param picture: a 2D char array
    @param N: an integer
    @return: return a integer
    """
    def findBlackPixel(self, picture, N):
        m = len(picture)
        n = len(picture[0])
        
        blks = [[[0, 0] for x in range(n)] for y in range(m)]
        
        for y, line in enumerate(picture):
            cnt = line.count('B')
            for x in range(n):
                blks[y][x][1] = cnt
        
        for x in range(n):
            cnt = 0
            for y in range(m):
                if picture[y][x] == 'B':
                    cnt += 1
            
            for y in range(m):
                blks[y][x][0] = cnt
        
        res = 0
        for y in range(m):
            for x in range(n):
                if picture[y][x] != 'B':
                    continue
                if blks[y][x][0] == N and blks[y][x][1] == N:
                    res += 1
        
        return res


stime = time.time()
# print(6 == Solution().findBlackPixel([
#     "WBWBBW",
#     "WBWBBW", 
#     "WBWBBW",
#     "WWBWBW"], 3))

print(1 == Solution().findBlackPixel([
    "WWW",
    "WWW",
    "WWB"], 1))
print(0 == Solution().findBlackPixel(["BBB","BBB","BBB"], 2))
print('elapse time: {} sec'.format(time.time() - stime))
