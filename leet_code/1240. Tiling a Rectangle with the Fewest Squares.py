
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        dp = [[0]*(n + 1) for i in range(m + 1)]


        def minimumSquare(m, n): 
            min_x = float('inf')
            min_y = float('inf')
              
            if m == n:
                return 1
                  
            if dp[m][n] != 0:
                return dp[m][n]
                  
            # The rectangle is cut horizontally and  
            # vertically into two parts and the cut  
            # with minimum value is found for every  
            # recursive call.
            for y in range(1, m//2 + 1):
                  
                # Calculating the minimum answer for the  
                # rectangles with width equal to n and length  
                # less than m for finding the cut point for  
                # the minimum answer 
                min_y = min(minimumSquare(y, n) + minimumSquare(m - y, n), min_y)

            for x in range(1, n//2 + 1): 
                  
                # Calculating the minimum answer for the  
                # rectangles with width equal to n and length  
                # less than m for finding the cut point for  
                # the minimum answer 
                min_x = min(minimumSquare(m, x) + minimumSquare(m, n - x), min_x)
                                 
            dp[m][n] = min(min_x, min_y) 
            return dp[m][n] 

        return minimumSquare(m, n)


stime = time.time()
# print(4 == Solution().maxLength(["un","iq","ue"]))
# print(26 == Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(5 == Solution().tilingRectangle(n = 5, m = 8))
#print(6 == Solution().tilingRectangle(n = 11, m = 13))
print('elapse time: {} sec'.format(time.time() - stime))