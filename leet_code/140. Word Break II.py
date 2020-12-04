
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
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
    
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        def dfs(s):
            if s in mem:
                return mem[s]

            if not s:
                return ['']
            res = []
            
            for i in range(len(s) + 1):
                if s[:i] in wordDict:
                    for item in dfs(s[i:]):
                        if not item:
                            res += s[:i],
                        else:
                            res += s[:i] + ' ' + item,

            mem[s] = res
            return res
        
        mem = {}
        return dfs(s)


stime = time.time()
print(["cats and dog","cat sand dog"] == Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print('elapse time: {} sec'.format(time.time() - stime))