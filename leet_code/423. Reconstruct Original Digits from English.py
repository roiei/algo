
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def originalDigits(self, s: str) -> str:
        unique_one = collections.defaultdict(tuple)
        unique_one['z'] = ('zero', 4, '0')  # string, len, digit
        unique_one['w'] = ('two', 3, '2')
        unique_one['u'] = ('four', 4, '4')
        unique_one['x'] = ('six', 3, '6')
        unique_one['g'] = ('eight', 5, '8')
        
        unique_two = collections.defaultdict(tuple)
        unique_two['o'] = ('one', 3, '1')
        unique_two['h'] = ('three', 5, '3')
        unique_two['f'] = ('five', 4, '5')
        unique_two['s'] = ('seven', 5, '7')
        
        unique_thr = collections.defaultdict(tuple)
        unique_thr['n'] = ('nine', 4, '9')
        
        uniques = [unique_one, unique_two, unique_thr]
        
        res = ''
        s = list(s)
        while s:
            for unique in uniques:

                pre = s[:]

                while True:
                    for key, values in unique.items():
                        if key not in s:
                            continue

                        digit_str = values[0]
                        n = values[1]
                        digit_num = values[2]
                        
                        i = 0
                        while s and i < n and digit_str[i] in s:
                            s.remove(digit_str[i])
                            i += 1
                        
                        res += digit_num

                    if pre == s:
                        break
                    pre = s[:]
        
        return ''.join(sorted(res))

    def originalDigits(self, s: str) -> str:
        unique = collections.defaultdict(int)
        unique['0'] = s.count('z')
        unique['2'] = s.count('w')
        unique['4'] = s.count('u')
        unique['6'] = s.count('x')
        unique['8'] = s.count('g')

        unique['1'] = s.count('o') - unique['4'] - unique['2'] - unique['0']
        unique['3'] = s.count('h') - unique['8']
        unique['5'] = s.count('f') - unique['4']
        unique['7'] = s.count('s') - unique['6']
        unique['9'] = s.count('i') - unique['5'] - unique['8'] - unique['6']

        res = ''
        for i in range(10):
            i = str(i)
            res += i*unique[i]
        return res

   

stime = time.time()
#print("012" == Solution().originalDigits("owoztneoer"))
#print("9" == Solution().originalDigits("nnei"))
print("00" == Solution().originalDigits("zerozero"))
print('elapse time: {} sec'.format(time.time() - stime))