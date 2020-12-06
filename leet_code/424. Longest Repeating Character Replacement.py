
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx = 0
        idxs = collections.defaultdict(list)

        if len(set(s)) == 1:
            return len(s)

        for ch in set(s):
            idxs[ch] += -1,
            idxs[ch] += k,
        
        for i, ch in enumerate(s):
            for k, v in idxs.items():
                if k != ch and idxs[k][1]:
                    idxs[k][1] -= 1

            length = i - idxs[ch][0]
            mx = max(length, mx)

            if idxs[ch][1] == 0:
                idxs[ch][0] = i

        
        length = i - idxs[ch][0]
        mx = max(length, mx)
        return mx


    def characterReplacement(self, s, k):
        mx = res = 0
        count = collections.Counter()

        for i, ch in enumerate(s):
            count[ch] += 1
            mx = max(mx, count[ch])

            if res - mx < k:
                res += 1
            else:
                count[s[i - res]] -= 1

        return res


    def characterReplacement(self, s, k):
        if not s:
            return 0
        
        r = l = 0
        freq = collections.Counter()
        
        for r, ch in enumerate(s):
            freq[ch] += 1
            mx = freq.most_common(1)[0][1]

            if r - l + 1 - mx > k:
                freq[s[l]] -= 1
                l += 1
                
        return r - l + 1

    def characterReplacement(self, s, k):
        if not s:
            return 0

        freq = collections.defaultdict(int)
        mx = 0
        l = 0
        
        for r, ch in enumerate(s):
            freq[ch] += 1
            mx = max(mx, freq[ch])
            
            while r - l + 1 - mx > k:
                freq[s[l]] -= 1
                l += 1
            
        return r - l + 1


stime = time.time()
print(4 == Solution().characterReplacement(s = "ABAB", k = 2))
print(4 == Solution().characterReplacement(s = "AABABBA", k = 1))
print(4 == Solution().characterReplacement("AAAA", 0))
print(3 == Solution().characterReplacement("AAAB", 0))
print('elapse time: {} sec'.format(time.time() - stime))

