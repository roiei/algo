import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.split('\s|,', paragraph)

        for i in range(len(words)):
            filtered = ''
            for ch in words[i]:
                if ch.isalpha() == True or ch == ' ':
                    filtered += ch
            words[i] = filtered
        
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        words = [[k, v] for k, v in freq.items() if k != '']
        words.sort(key=lambda p:p[1], reverse=True)
        for w in words:
            if w[0] not in banned:
                return w[0]
        return None

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def filter(word):
            res = ''
            for letter in word:
                if letter.isalpha():
                    res += letter
            return res

        paragraph = [filter(word) for word in re.split('\s|,', paragraph.lower())]
        freq = collections.Counter(paragraph)
        words = [[k, v] for k, v in freq.items() if k]
        freq = sorted(words, key=lambda p: p[1], reverse=True)
        
        for k, v in freq:
            if k not in banned:
                return k

        return ''


stime = time.time()
print('ball' == Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
print('b' == Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
print('elapse time: {} sec'.format(time.time() - stime))