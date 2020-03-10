
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = map(int, date1.split('-'))
        year2, month2, day2 = map(int, date2.split('-'))
        
        leap_year     = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def is_leap(year):
            return year%400 == 0 or (year%4 == 0 and year%100 != 0)
        
        def get_days(year_in, month_in, day_in):
            days = 0
            for year in range(1971, year_in):
                days += 365
                days += 1 if is_leap(year) else 0

            months = leap_year if is_leap(year_in) else non_leap_year
            for i in range(month_in - 1):
                days += months[i]
            days += day_in
            return days
        
        days1 = get_days(year1, month1, day1)
        days2 = get_days(year2, month2, day2)
        return abs(days1 - days2)
            
            
stime = time.time()
print(15 == Solution().daysBetweenDates("2020-01-15", "2019-12-31"))
print('elapse time: {} sec'.format(time.time() - stime))