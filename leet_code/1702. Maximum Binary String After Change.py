import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        lo = 0
        for i in range(len(binary)):
            if binary[i] != '1':
                break
            lo += 1

        # cnt = 0
        # binary = list(binary)
        # for i in range(len(binary) - 2, -1 + lo, -1):
        #     if binary[i] + binary[i + 1] == '10':
        #         binary[i] = '0'
        #         binary[i + 1] = '1'
        #         cnt += 1

        # 000110
        #     --
        # 000101
        #    --
        # 000011

        zeros = binary.count('0')
        ones = binary.count('1')

        if zeros < 2:
            return ''.join(binary)

        print(zeros, cnt)
        res = lo*'1' + (zeros - 1)*'1' + '0' + (ones - lo)*'1'
        print(res)
        return res
        

stime = time.time()
#print("111011" == Solution().maximumBinaryString("000110"))
#print("01" == Solution().maximumBinaryString("01"))
#print("1110" == Solution().maximumBinaryString("1100"))
print("1111111111110111111111111" == Solution().maximumBinaryString("0000011010101011111001001"))
print('elapse time: {} sec'.format(time.time() - stime))
