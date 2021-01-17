import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = collections.defaultdict(list)
        visited = set()
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '@' + word[i + 1:]
                g[key] += word,
        
        q = [(beginWord, [beginWord])]
        res = set()
        
        while q:
            word, trace = q.pop(0)
            visited.add(word)
            if word == endWord:
                res.add(tuple(trace))

            for i in range(len(word)):
                key = word[:i] + '@' + word[i + 1:]
                for v in g[key]:
                    if v in visited:
                        continue
                    
                    q += (v, trace + [v]),
        
        if not res:
            return None

        res = sorted(res, key=len)
        ret = [list(res.pop(0))]
        for i in range(len(res)):
            if len(res[i]) != len(ret[-1]):
                break
            ret += list(res[i]),

        return ret
        

stime = time.time()
print([
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
] == Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
#print(0 == Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
#print(2 == Solution().ladderLength("hot", "dot", ["hot","dot","dog"]))
print('elapse time: {} sec'.format(time.time() - stime))