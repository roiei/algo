import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = collections.defaultdict(list)
        visited = set()
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '@' + word[i + 1:]
                g[key] += word,
        
        q = [(beginWord, 1)]
        diff = 0
        
        while q:
            word, diff = q.pop(0)
            if word == endWord:
                break

            for i in range(len(word)):
                key = word[:i] + '@' + word[i + 1:]
                for v in g[key]:
                    if v in visited:
                        continue
                    
                    q += (v, diff + 1),
                    visited.add(v)
        
        return diff if word == endWord else 0
        

stime = time.time()
#print(5 == Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
#print(0 == Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
print(2 == Solution().ladderLength("hot", "dot", ["hot","dot","dog"]))
print('elapse time: {} sec'.format(time.time() - stime))
