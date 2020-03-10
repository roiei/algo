import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        if not words:
            return 0
        freq = {}
        for w in words:
            if w not in freq:
                freq[w] = 0
            freq[w] += 1
        res = sorted(freq.items(), key=lambda p:p[1], reverse=True)
        outs = []
        out = []
        ccnt = res[0][1]
        for key,v in res:
            if v == ccnt:
                out += key,
            else:
                outs += out,
                out = [key]
            ccnt = v
        outs += out,

        out = []
        i = j = 0
        while i < len(outs) and k > 0:
            outs[i].sort()
            j = 0
            while j < len(outs[i]) and k > 0:
                out += outs[i][j],
                k -= 1
                j += 1
            i += 1
        return out
            

stime = time.time()
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
#print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
print('elapse time: {} sec'.format(time.time() - stime))