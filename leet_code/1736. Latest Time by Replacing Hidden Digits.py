import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = map(list, time.split(':'))

        if hour[0] == '?':
            if hour[1] != '?' and hour[1] >= '4':
                hour[0] = '1'
            else:
                hour[0] = '2'
                if hour[1] == '?':
                    hour[1] = '3'
        else:
            if hour[0] == '2':
                if hour[1] == '?':
                    hour[1] = '3'
            elif hour[1] == '?':
                hour[1] = '9'

        if minute[0] == '?':
            minute[0] = '5'

        if minute[1] == '?':
            minute[1] = '9'

        return ''.join(hour) + ':' + ''.join(minute)

"??:3?"
stime = time.time()
print("00:01" == Solution().maximumTime("00:01"))
print("14:03" == Solution().maximumTime("?4:03"))
print("23:50" == Solution().maximumTime("2?:?0"))
print("09:39" == Solution().maximumTime("0?:3?"))
print("19:22" == Solution().maximumTime("1?:22"))

print('elapse time: {} sec'.format(time.time() - stime))
