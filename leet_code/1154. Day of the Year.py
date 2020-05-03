
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def dayOfYear(self, date: str) -> int:
        leap_year =     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_day_of_year(year, month, day):
            month_tbl = non_leap_year
            if 0 == year%400 or (year%4 == 0 and year%100 != 0):
                month_tbl = leap_year

            count = 0
            for i in range(month - 1):
                count += month_tbl[i]
            count += day

            return count
        
        count = get_day_of_year(year, month, day)
        
        for i in range(1971, year):
            count += 365
            if 0 == i%400 or (i%4 == 0 and i%100 != 0):
                count += 1
        
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
        return week[(count + 4)%7]


        
        date =  list(map(int, date.split('-')))
        return get_day_of_year(date[0], date[1], date[2])


stime = time.time()
print(9 == Solution().dayOfTheWeek(date = "2019-01-09"))
print(41 == Solution().dayOfTheWeek(date = "2019-02-10"))
print('elapse time: {} sec'.format(time.time() - stime))