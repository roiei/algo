
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split()
        for i, word in enumerate(sentences):
            if word.startswith(searchWord):
                return i + 1
        return -1

                


stime = time.time()
print(4 == Solution().isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
print('elapse time: {} sec'.format(time.time() - stime))