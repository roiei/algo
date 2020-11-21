import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


# Given two positive integers n and k, the binary string  Sn is formed as follows:

# S1 = "0"
# Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first 4 strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(seq):
            return ''.join(['0' if ch == '1' else '1' for ch in seq])

        s = "0"
        n -= 1

        while n:
            s = s + '1' + invert(s)[::-1]
            n -= 1

        return s[k - 1]


stime = time.time()
print("0" == Solution().findKthBit(n = 3, k = 1))
print("1" == Solution().findKthBit(n = 4, k = 11))
print("0" == Solution().findKthBit(n = 1, k = 1))
print("1" == Solution().findKthBit(n = 2, k = 3))
print('elapse time: {} sec'.format(time.time() - stime))