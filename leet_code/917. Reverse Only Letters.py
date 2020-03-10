import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:        
        rs = [ch for ch in list(S)[::-1] if ('a' <= ch <= 'z' or 'A' <= ch <= 'Z')]
        nonletters = []
        for i, ch in enumerate(S):
            if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
                nonletters += (i, ch),
            
        for pos, ch in nonletters:
            rs.insert(pos, ch)
        return ''.join(rs)


stime = time.time()
print('dc-ba' == Solution().reverseOnlyLetters('ab-cd'))
print("Qedo1ct-eeLg=ntse-T!" == Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print('elapse time: {} sec'.format(time.time() - stime))

