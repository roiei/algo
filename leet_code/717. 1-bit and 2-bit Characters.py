import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def isOneBitCharacter(self, bits):
        last_bit_cnt = 0
        codes = ['0', '10', '11']
        
        while bits:
            bit = bits.pop(0)
            sec_bit = ''
            last_bit_cnt = 1
            
            if bit == 1:
                sec_bit = bits.pop(0)
                last_bit_cnt = 2
            
            if str(bit) + str(sec_bit) in codes:
                continue
        
        return last_bit_cnt == 1


stime = time.time()
print(False == Solution().isOneBitCharacter([1,1,1,0]))
print('elapse time: {} sec'.format(time.time() - stime))


