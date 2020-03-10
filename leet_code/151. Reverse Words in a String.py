import time
from util_list import *
from util_tree import *
import copy
import collections




class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])




stime = time.time()
print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world!  "))
print(Solution().reverseWords("a good   example"))
print('elapse time: {} sec'.format(time.time() - stime))