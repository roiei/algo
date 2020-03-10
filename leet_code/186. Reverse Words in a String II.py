import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        return ' '.join(str.split()[::-1])


stime = time.time()

print("blue is sky the" == Solution().reverseWords("the sky is blue"))
print('elapse time: {} sec'.format(time.time() - stime))