
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        n = len(s)
        i = j = 0        
        length = 0
        freq = collections.defaultdict(int)
        freq_ss = collections.defaultdict(int)
        
        while i < n:
            print(freq)

            freq[s[i]] += 1
            i += 1
            
            while len(freq) > maxLetters:
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j += 1

            while i - j > maxSize:
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j += 1

            length = i - j

            print('i = {}, j = {}, kind = {}, length = {}'.format(i, j, len(freq), length))
            print(freq)
            
            if minSize <= length <= maxSize and len(freq) <= maxLetters:
                freq_ss[s[j:i]] += 1

            print('freq_ss = ', freq_ss, end = '\n\n')
        
        res = sorted(freq_ss.items(), key=operator.itemgetter(1, 0), reverse=True)
        print(res)
        return res[0][1]


    def maxFreq(self, s, maxLetters, minSize, maxSize):
        mx = 0
        freq = collections.defaultdict(int)
        
        for i in range(len(s) - minSize + 1):
            freq[s[i:i + minSize]] += 1
            
        for substr in freq:
            if len(set(substr)) <= maxLetters and mx < freq[substr]:
                mx = freq[substr]
        
        return mx

            
stime = time.time()
#print(2 == Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
print(0 == Solution().maxFreq("abcde", 2, 3, 3))
print('elapse time: {} sec'.format(time.time() - stime))