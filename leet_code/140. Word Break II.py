
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        
        def recur(s, wordDict):
            if s in memo:
                return memo[s]

            res = []

            for i in range(len(s)):
                first, second = s[:i+1], s[i+1:]
                if first in wordDict:
                    if second == "":
                        res += first, 
                    else:
                        ret = recur(second, wordDict)
                        for i in range(len(ret)):
                            res += first + " " + ret[i],

            memo[s] = res
            return res
        
        memo = {}
        ret = recur(s, wordDict)
        return ret
        

stime = time.time()
print(["cats and dog","cat sand dog"] == Solution().removeZeroSumSublists("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print('elapse time: {} sec'.format(time.time() - stime))