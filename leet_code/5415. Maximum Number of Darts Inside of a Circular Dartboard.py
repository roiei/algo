
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections
import math 


class Solution:
    def numPoints(self, points: [[int]], r: int) -> int:

        # Computing the x^2 + y^2 for each 
        # given points and sorting them. 
        def preprocess(p, x, y, n): 
            for i in range(n): 
                p[i] = x[i] * x[i] + y[i] * y[i] 

            p.sort() 

        def query(p, n, rad): 
            start = 0
            end = n - 1
            while ((end - start) > 1): 
                mid = (start + end) // 2
                tp = math.sqrt(p[mid]) 

                if (tp > (rad * 1.0)): 
                    end = mid - 1
                else: 
                    start = mid 

            tp1 = math.sqrt(p[start]) 
            tp2 = math.sqrt(p[end]) 

            if (tp1 > (rad * 1.0)): 
                return 0
            elif (tp2 <= (rad * 1.0)): 
                return end + 1
            else: 
                return start + 1

        p = [0]*len(points)

        x_points = []
        y_points = []
        for x, y in points:
            x_points += x,
            y_points += y,

        preprocess(p, x_points, y_points, len(points)) 
        return query(p, len(points), r)



stime = time.time()
print(4 == Solution().numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2))
print(5 == Solution().numPoints([[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5))
print('elapse time: {} sec'.format(time.time() - stime))