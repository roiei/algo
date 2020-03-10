
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        i = 0
        j = 0
        cnt = collections.defaultdict(int)
        mx = 0
        num = 0
        
        while i < n:
            cnt[s[i]] += 1
            num += 1
            
            while len(cnt) > k:
                if cnt[s[j]] > 0:
                    cnt[s[j]] -= 1
                    num -= 1
                    if cnt[s[j]] == 0:
                        del cnt[s[j]]
                j += 1

            mx = max(mx, num)
            i += 1
        
        return mx


stime = time.time()
print(4 == Solution().lengthOfLongestSubstringKDistinct(S = "eceba" and k = 3)) # "eceb"
print(4 == Solution().lengthOfLongestSubstringKDistinct(S = "WORLD" and k = 4)) # "WORL" or "ORLD"
print('elapse time: {} sec'.format(time.time() - stime))