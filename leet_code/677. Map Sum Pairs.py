import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.child = {}
        self.eow = False
        self.val = 0


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
        node = self.root

        for ch in prefix:
            if ch not in node.child:
                return 0

            node = node.child[ch]

        tot = 0
        q = [node]
        while q:
            node = q.pop(0)
            if node.eow:
                tot += node.val

            for child in node.child:
                q += node.child[child],

        return tot
