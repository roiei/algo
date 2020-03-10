import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        sx = max(A, E)
        ex = min(C, G)
        sy = max(B, F)
        ey = min(D, H)
        
        area_a = (C - A)*(D - B)
        area_b = (G - E)*(H - F)

        if not ((A <= sx <= ex <= C and E <= sx <= ex <= G) and 
           (B <= sy <= ey <= D and F <= sy <= ey <= H)):
            return area_a + area_b
        

        return area_a + area_b - ((ex - sx)*(ey - sy))


stime = time.time()
print(20 == Solution().computeArea(-2,-2,2,2,-1,4,1,6))
print('elapse time: {} sec'.format(time.time() - stime))