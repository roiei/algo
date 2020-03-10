import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def romanToInt(self, s: str) -> int:
        out = []
        kinds = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, \
                'C' : 100, 'XC' : 90, 'L' : 50, 'XL' : 40, \
                'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4}
        s = list(s)
        num = 0

        while s:
            snum1 = s.pop(0)
            snum2 = ''
            
            if s:
                snum2 = s.pop(0)
            
            print(snum1 + snum2)
            
            if snum1 + snum2 in kinds:
                num += kinds[snum1 + snum2]
            else:
                if '' != snum2:
                    s.insert(0, snum2)
                
                if snum1 in kinds:
                    num += kinds[snum1]
                else:
                    if snum1 == 'I':
                        cnt = 1
                        while s and s[-1] == 'I':
                            snum1 += s.pop(0)
                            cnt += 1
                        num += cnt

        return num


stime = time.time()
#print(4 == Solution().romanToInt("IV"))
print(Solution().romanToInt("DCXXI"))
print('elapse time: {} sec'.format(time.time() - stime))


