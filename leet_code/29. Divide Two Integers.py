import time
#from util_list import *
from util.util_tree import *


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign_dividened = -1 if dividend < 0 else 1
        sign_divisor = -1 if divisor < 0 else 1

        if -2147483648 == dividend and -1 == divisor:  # for wrong TC (989/989)
            return 2147483647

        dividend = abs(dividend)        
        divisor = abs(divisor)
        divs = []
        cnt = 0
        quotient = 1

        while dividend >= (divisor<<cnt):
            print('divisor = {}'.format(divisor<<cnt))
            divs.append([divisor<<cnt, quotient])
            quotient <<= 1
            cnt += 1
            print('divisor = {}'.format(divisor<<cnt))
            print()
        cnt = 0

        print(divs)

        while dividend >= divisor:
            for div in divs:
                if dividend >= div[0]:
                    dividend -= div[0]
                    cnt += div[1]
        print('cnt = {}, sign_dividened = {}, sign_divisor = {}'.format(cnt, sign_dividened, sign_divisor))
        return cnt*sign_dividened*sign_divisor


stime = time.time()
print('sol = ', Solution().divide(10, 3))
#print('sol = ', Solution().divide(100, 3))
# print(Solution().divide(14, 3))
# print(Solution().divide(-1, 1))
#print(Solution().divide(-2147483648, -1))
#print(Solution().divide(2147483647, 2))
print('elapse time: {} sec'.format(time.time() - stime))

