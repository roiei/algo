import time
from util_list import *
from util_tree import *
import copy
import collections



class Solution(object):
    def hasAlternatingBits_es(self, n):
        sn = '{:b}'.format(n)
        pch = None
        print(sn)
        for i, ch in enumerate(sn):
            print(pch, ch)
            if pch == ch:
                return False
            pch = ch
        return True

    def hasAlternatingBits(self, n):
        sn = bin(n)
        length = len(sn[2:])
        odd_mask = [0]*length
        even_mask = [0]*length
        full = int('0b'+''.join(['1']*length), 2)
        for i in range(length):
            if 0 == i%2:
                even_mask[i] = 1
            else:
                odd_mask[i] = 1
        cnt1 = n^int('0b'+''.join([str(bit) for bit in even_mask]), 2)
        cnt2 = n^int('0b'+''.join([str(bit) for bit in odd_mask]), 2)

        print(n, full)
        print(cnt1, cnt2)

        if (cnt1 == 0 or cnt1 == full) and (cnt2 == 0 or cnt2 == full):
            return True
        return False



stime = time.time()
print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
print('elapse time: {} sec'.format(time.time() - stime))