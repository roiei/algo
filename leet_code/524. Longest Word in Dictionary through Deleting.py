
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def findLongestWord(self, s: str, d: [str]) -> str:
        d.sort(key=lambda p: (-len(p), p))
        res = []
        for word in d:
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1

            if j == len(word):
                return word

        return ''


stime = time.time()
print("ab" == Solution().findLongestWord("bab", ["ba","ab","a","b"]))
print("apple" == Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
print("ewaf" == Solution().findLongestWord("aewfafwafjlwajflwajflwafj", ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]))
print('elapse time: {} sec'.format(time.time() - stime))

