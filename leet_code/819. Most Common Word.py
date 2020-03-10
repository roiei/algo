import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


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
        print(freq)
        words = [[k, v] for k, v in freq.items() if k != '']
        words.sort(key=lambda p:p[1], reverse=True)
        print(words)
        for w in words:
            if w[0] not in banned:
                return w[0]
        return None



stime = time.time()
print('ball' == Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
print('elapse time: {} sec'.format(time.time() - stime))