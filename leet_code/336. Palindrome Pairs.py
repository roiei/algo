import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.index = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, i):
        node = self.root
        for ch in word:
            node = node.child[ch]
        node.isEnd = True
        node.index = i
    
    def search(self, word):
        node = self.root
        for ch in word:
            node = node.child[ch]
            if not node:
                return (False, -1)
        return (node.isEnd, node.index)
    

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if len(words) == 0:
            return []
        
        res = []
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                s1, s2 = word[:j], word[j:]
                if self.valid(s1):
                    flag, idx = trie.search(s2[::-1])
                    if flag and idx != i:
                        res.append([idx, i])
                if len(s2) > 0 and self.valid(s2):
                    flag, idx = trie.search(s1[::-1])
                    if flag and idx != i:
                        res.append([i, idx])

        return res
                    
    def valid(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


stime = time.time()
print([[1,0],[0,1],[3,2],[2,4]] == Solution().palindromePairs(words = ["abcd","dcba","lls","s","sssll"]))
print('elapse time: {} sec'.format(time.time() - stime))
