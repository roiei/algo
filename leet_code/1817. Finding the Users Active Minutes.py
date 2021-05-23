
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

# Return the array answer as described above.

# logs[i] = [IDi, timei]  # user ID, action time
# UAM: 


# 1 2 3 4 5 6
#   1 1   0
#   0 


# the number of occurance of user's total amonut of active minutes
# if A user's UAM is 2
# then [1] += 1
#
# if B user's UAM is 3
# then [2] += 1


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0]*k
        
        users_uam = collections.defaultdict(int)
        for uid, min in {(uid, min) for uid, min in logs}:
            users_uam[uid] += 1

        for uid, min in users_uam.items():
            res[min - 1] += 1

        return res


stime = time.time()
print([0,2,0,0,0] == Solution().findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
print('elapse time: {} sec'.format(time.time() - stime))