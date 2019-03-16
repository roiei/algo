
leap_year     = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_data_of_year(year, month):
    days = 0
    month_tbl = leap_year if 0 == year % 4 or 0 != year % 100 else non_leap_year
    for i in range(month - 1):
        days += month_tbl[i]
    return days

def get_diff_date(date1, date2):
    days = (int(date1[:4]) - int(date2[:4]))*365
    days1 = get_data_of_year(year1, int(date1[4:6])) + int(date1[6:])
    days2 = get_data_of_year(year2, int(date2[4:6])) + int(date2[6:])
    return days + days1 - days2

date1 = input('input date1: ')
date2 = input('input date2: ')

if int(date1) < int(date2):
    date1, date2 = date2, date1
print(get_diff_date(date1, date2))


