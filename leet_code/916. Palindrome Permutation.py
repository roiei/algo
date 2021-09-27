import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        freq = collections.Counter(s)
        odd = 0

        for k, v in freq.items():
            if v%2 != 0:
                if odd:
                    return False
                odd += 1

        return True


print(True == Solution().canPermutePalindrome("aab"))
print(False == Solution().canPermutePalindrome("code"))
print(True == Solution().canPermutePalindrome("carerac"))
