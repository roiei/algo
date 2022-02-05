import time
from util.util_list import *
from util.util_tree import *
from typing import List
import copy
import collections


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def updateFrequency(sentence, freq):
            for word in sentence.split():
                if word not in freq:
                    freq[word] = 0

                freq[word] += 1
        
        freq = {}
        updateFrequency(s1, freq)
        updateFrequency(s2, freq)
        
        res = []
        for item, num in freq.items():
            if 1 == num:
                res.append(item)
        
        return res

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = collections.Counter(s1.split()) + collections.Counter(s2.split())
        return [item for item, num in freq.items() if num == 1]



stime = time.time()
print(['expensive', 'adorable'] == Solution().uncommonFromSentences(s1 = "I have an expensive doll", s2 = "I have an adorable doll"))
print('elapse time: {} sec'.format(time.time() - stime))