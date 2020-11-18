import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
Two strings are considered close 
if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into 
another existing character, and do the same with the other character.

For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
    a:3, c:1, b:2
    b:3, c:1, a:2

Given two strings, word1 and word2, return true if word1 and word2 are close, 
and false otherwise.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = collections.Counter(word1)
        b = collections.Counter(word2)

        return sorted(a.values()) == sorted(b.values()) and \
            sorted(a.keys()) == sorted(b.keys())
 

stime = time.time()
#print(True == Solution().closeStrings(word1 = "abc", word2 = "bca"))
print(False == Solution().closeStrings("uau", "ssx"))
print('elapse time: {} sec'.format(time.time() - stime))