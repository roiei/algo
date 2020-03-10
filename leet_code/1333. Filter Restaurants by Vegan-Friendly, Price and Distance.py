
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def filterRestaurants(self, restaurants: [[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> [int]:
        
        res = []
        for _id, rate, is_vegan, mx_price, mx_distance in restaurants:
            if not (veganFriendly == 1 and is_vegan == 1) and not (veganFriendly == 0):
                continue
                
            if mx_price <= maxPrice and mx_distance <= maxDistance:
                res += (_id, rate, is_vegan),

        res.sort(key=lambda p: p[1], reverse=True)
        rates = collections.defaultdict(list)

        for _id, rate, is_vegan in res:
            rates[rate] += _id,

        res = []
        for rate, ids in rates.items():
            ids.sort(reverse=True)
            res += ids

        return res

            
stime = time.time()
#print([3,1,5]  == Solution().filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10))
print([4,3,2,1,5] == Solution().filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 50, 10))
print('elapse time: {} sec'.format(time.time() - stime))