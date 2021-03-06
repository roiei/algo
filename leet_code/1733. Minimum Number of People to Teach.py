import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools
from typing import List


# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        1: 1, 3
        2: 2, 3

        1: 2, 3
        2: 1, 3
        3: 2, 4



stime = time.time()
print(1 == Solution().minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))
print(2 == Solution().minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))
print('elapse time: {} sec'.format(time.time() - stime))