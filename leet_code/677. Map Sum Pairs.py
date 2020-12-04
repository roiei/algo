import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.eow = True
        self.val = 0
        self.child = {}


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for ch in key:
            if ch not in cur.child:
                cur.child[ch] = TrieNode(ch)
            cur = cur.child[ch]
        
        cur.eow = True
        cur.val = val
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]
        
        q = [cur]
        cnt = 0
        
        while q:
            node = q.pop(0)
            if node.eow == True:
                cnt += node.val
            
            for k, v in node.child.items():
                q += v,
        
        return cnt

