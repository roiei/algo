year = 2100 # 13.09.2100
# year = 1984
year = 1918
 
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30]
non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30]
 
def is_leap_year(year):
    official_type = ''
    if year >= 1700 and year <= 1917:
        official_type = 'Julian'
    elif year == 1918:
        # 1.31 -> 2.14
        official_type = 'Gregorian'
    elif year >= 1919:
        official_type = 'Gregorian'
    else:
        official_type = 'Julian'
    print(official_type)
    leap_year = False
    if official_type == 'Julian':
        leap_year = True if year % 4 == 0 else False
    elif official_type == 'Gregorian':
        leap_year = True if 0 == year % 400 or (year % 4 == 0 and year % 100 != 0) else False
    print(year / 400)
    print(year / 4)
    print(year / 100)
    print(leap_year)
    return leap_year
 
def dayOfProgrammer(year):
    month_tbl = non_leap_year
    if True == is_leap_year(year):
        print('leap_year')
        month_tbl = leap_year
    acc = 0
    m = 0
    day_offset = 0
    print('year = ', year)
    if year == 1918:
        day_offset = 13
    try:
        while 256 > (acc + month_tbl[m]) and m < len(month_tbl):
            acc += month_tbl[m]
            m += 1
            print('m = {}, acc = {}'.format(m, acc))
    except IndexError as e:
        print('m : ', m)
 
    day = 256 - acc
    print('{:02}.{:02}.{:04}'.format(day + day_offset, m + 1, year))
    return str('{:02}.{:02}.{:04}'.format(day + day_offset, m + 1, year))
 
dayOfProgrammer(year)