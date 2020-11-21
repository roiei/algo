import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        i = 0
        space = 0

        while i < n:
            if not text[i].isalpha():
                space += 1
            i += 1

        text = text.split()
        divisor = len(text) - 1

        if divisor > 0:
            even = space//divisor
        else:
            even = space
        left = space - even*divisor
        fmt = ' '*even
        text = fmt.join(text)
        text += ' '*left
        return text


stime = time.time()
print("this   is   a   sentence" == Solution().reorderSpaces(text = "  this   is  a sentence "))
print("practice   makes   perfect " == Solution().reorderSpaces(" practice   makes   perfect"))
print('elapse time: {} sec'.format(time.time() - stime))

# "  this   is  a sentence "

# 9/4 -> floating...
# 9/3 -> 3

# Input: text = "  walks  udp package   into  bar a"  11/5 = 2
# Output: "walks  udp  package  into  bar  a "