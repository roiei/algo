
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        leap_year =     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_day_of_year(year, month, day):
            month_tbl = non_leap_year
            if 0 == year % 400 or (year % 4 == 0 and year % 100 != 0):
                month_tbl = leap_year

            count = 0
            for i in range(month - 1):
                count += month_tbl[i]
            count += day

            return count
        
        count = get_day_of_year(year, month, day)
        
        for i in range(1971, year):
            count += 365
            if 0 == i % 400 or (i % 4 == 0 and i % 100 != 0):
                count += 1
        
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
        return week[(count + 4)%7]


stime = time.time()
print("Saturday" == Solution().dayOfTheWeek(day = 31, month = 8, year = 2019))
print("Sunday" == Solution().dayOfTheWeek(day = 18, month = 7, year = 1999))
print('elapse time: {} sec'.format(time.time() - stime))