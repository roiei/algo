import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        cnt = 0
        for seat, student in list(zip(sorted(seats), sorted(students))):
            cnt += abs(seat - student)

        return cnt


stime = time.time()
print(4 == Solution().minMovesToSeat(seats = [3,1,5], students = [2,7,4]))
print('elapse time: {} sec'.format(time.time() - stime))