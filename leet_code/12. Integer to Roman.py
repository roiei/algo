import time
from util_list import *


class Solution:
    def intToRoman(self, num: int) -> str:
        out = []
        kinds = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], 
                [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], 
                [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV']]

        while num > 0:
            for k in kinds:
                if k[0] <= num:
                    cnt = num // k[0]
                    out.append(cnt*k[1])
                    num %= k[0]
            if 0 < num < 4:
                out.append(num*'I')
                num = 0

        return ''.join(out)



stime = time.time()
# print(Solution().intToRoman(3))
# print(Solution().intToRoman(4))
# print(Solution().intToRoman(9))
# print(Solution().intToRoman(58))
print('X' == Solution().intToRoman(10))
print("MCMXCIV" == Solution().intToRoman(1994))
print('elapse time: {} sec'.format(time.time() - stime))
