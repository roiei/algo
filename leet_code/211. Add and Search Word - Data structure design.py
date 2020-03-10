
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.child = {}
        self.eow = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def add(self, word):
        if self.search(word):
            return

        node = self.root
        
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode(ch)
            node = node.child[ch]
        
        node.eow = True
    
    def sub_search(self, word, node):
        for i, ch in enumerate(word):
            if ch not in node.child and ch != '.':
                return False

            if ch == '.':
                for k in node.child.keys():
                    if self.sub_search(word[i + 1:], node.child[k]):
                        return True
            else:
                node = node.child[ch]
        
        return True if node.eow else False
            
    def search(self, word):
        node = self.root
        
        for i, ch in enumerate(word):
            if ch not in node.child and ch != '.':
                return False
            
            if ch == '.':
                if not node.child:
                    return False

                for k in node.child.keys():
                    if self.sub_search(word[i + 1:], node.child[k]):
                        return True
            else:
                node = node.child[ch]
        
        return True if node.eow else False
        

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        
ins = zip(["WordDictionary","addWord","addWord","search","search","search","search","search","search"], [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]], [None,None,None,True,True,False,True,False,False])

wd = None
for op, param, expected in ins:
    if op == 'WordDictionary':
        wd = WordDictionary()
    elif op == 'addWord':
        if expected != wd.addWord(param):
            print('False @ {} {} {}'.format(op, param, expected))
            break
    elif op == 'search':
        if expected != wd.search(param):
            print('False @ {} {} {}'.format(op, param, expected))
            break
else:
    print('True')


