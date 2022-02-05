import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math


class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.child = {}
        self.eow = False


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        cnt = 0

        root = TrieNode(None)
        for start in startWords:
            node = root

            for ch in sorted(start):
                if ch not in node.child:
                    node.child[ch] = TrieNode(ch)
                node = node.child[ch]
            node.eow = True

        for target in targetWords:
            target = sorted(target)

            for i in range(len(target)):
                word = target[:i] + target[i + 1:]

                node = root
                checked_len = 0
                for ch in word:
                    if ch not in node.child:
                        break
                    node = node.child[ch]
                    checked_len += 1

                if node.eow and checked_len == len(target) - 1:
                    cnt += 1
                    break
        
        return cnt


stime = time.time()
print(2 == Solution().wordCount(startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]))
print(1 == Solution().wordCount(startWords = ["ab","a"], targetWords = ["abc","abcd"]))
print('elapse time: {} sec'.format(time.time() - stime))