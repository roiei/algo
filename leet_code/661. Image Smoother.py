
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def imageSmoother(self, M: [[int]]) -> [[int]]:
        rows = len(M)
        cols = len(M[0])
        res = [[0]*cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                tot = 0
                cnt = 0
                
                for oy in range(y - 1, y + 2):
                    for ox in range(x - 1, x + 2):
                        if not (0 <= oy < rows and 0 <= ox < cols):
                            continue
                        
                        cnt += 1
                        tot += M[oy][ox]

                res[y][x] = math.floor(tot/cnt)
                
        return res
        

stime = time.time()
#print([[0, 0, 0], [0, 0, 0], [0, 0, 0]] == Solution().imageSmoother([[1,1,1], [1,0,1], [1,1,1]]))

print([[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]] == Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
print('elapse time: {} sec'.format(time.time() - stime))