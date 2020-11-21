import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def unhappyFriends(self, n: int, preferences: [[int]], pairs: [[int]]) -> int:
        pair_groups = collections.defaultdict(int)
        for i, pair in enumerate(pairs):
            x, y = pair
            pair_groups[x] = i
            pair_groups[y] = i
            
        cnt = 0
        for pair_idx, pair in enumerate(pairs):
            x, y = pair
            print(x, y)

            i = 0
            x_preference = preferences[x]
            while i < len(x_preference) and x_preference[i] != y:
                if pair_idx != pair_groups[x_preference[i]]:
                    cnt += 1
                    break
                i += 1

            print(cnt)
            
            i = 0
            y_preference = preferences[y]
            while i < len(y_preference) and y_preference[i] != x:
                if pair_idx != pair_groups[y_preference[i]]:
                    cnt += 1
                    break
                i += 1
        
            print(cnt)
            print()
        print(cnt)
        return cnt


stime = time.time()
#print(2 == Solution().unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]))
print(0 == Solution().unhappyFriends(4, [[1,3,2],[2,3,0],[1,0,3],[1,0,2]], [[2,1],[3,0]]))
print('elapse time: {} sec'.format(time.time() - stime))

