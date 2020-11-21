
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    # concept
    #   there is no heater at left then the left radius is to be INF
    #   for right-side, vise-versa

    #   for current house position, 
    #       take the closest distance from both left heater and right heater

    # 1    2    3    4 
    # 1              4 

    #       1:  try to find in [1, 4] -> found '0' idx
    #           but it is the first element, 
    #           left = 1 - -INF = INF
    #           rigt = 1 - 1 = 0
    #           radius = min(0, INF) = 0

    #       2:  '1' idx
    #           left = 2 - 1 = 1
    #           rigt = 4 - 2 = 2
    #           radius = min(1, 2) = 1 <- need to consider only the nearest one


    def findRadius(self, houses: [int], heaters: [int]) -> int:
        mx = 0
        heaters.sort()

        for house in houses:
            idx = bisect.bisect_left(heaters, house)

            if idx == 0:
                left = float('-inf')
            else:
                left = heaters[idx - 1]

            if idx == len(heaters):
                right = float('inf')
            else:
                right = heaters[idx]

            mx = max(mx, min(house - left, right - house))

        return mx

     # 1              5       1                 5
     #      2                      2

     # 1              5
     #                                                  10


stime = time.time()
# print(1 == Solution().findRadius([1,2,3,4], [1,4]))
# print(3 == Solution().findRadius([1,5], [2]))
# print(0 == Solution().findRadius([1], [1,2,3,4]))
print(9 == Solution().findRadius([1,5], [10]))
print('elapse time: {} sec'.format(time.time() - stime))
