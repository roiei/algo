import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        s = list(s)
        for i in range(len(s)//2):
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                left = s[:-1]
                right = s[1:]
                if left == left[::-1] or right == right[::-1]:
                    return True
                else:
                    return False
        return True
            

stime = time.time()
print(False == Solution().validPalindrome('abc'))
print(True == Solution().validPalindrome('abca'))
print('elapse time: {} sec'.format(time.time() - stime))