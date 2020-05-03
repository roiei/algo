
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
        if self.search(node=self.root, word=word):
            return

        node = self.root
        
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode(ch)
            node = node.child[ch]
        
        node.eow = True
            
    def search(self, node, word):
        for i, ch in enumerate(word):
            if not node.child:
                return False

            if ch not in node.child and ch != '.':
                return False
            
            if ch == '.':
                if not node.child:
                    return False

                res = []
                for k in node.child.keys():
                    res += self.search(node.child[k], word[i + 1:]),

                if any(res):
                    return True
                else:
                    return False  # !
            else:
                node = node.child[ch]
        
        return True if node.eow else False
        

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        print('\n+search')
        return self.trie.search(node=self.trie.root, word=word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


#case = zip(["WordDictionary","addWord","addWord","search","search","search","search","search","search"], [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]], [None,None,None,True,True,False,True,False,False])


#case = zip(["WordDictionary","addWord","addWord","search","search","search","search","search","search"], [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]], [None,None,None,True,True,False,True,False,False])

#case = zip(["WordDictionary","addWord","addWord","search",], ['',"a","a",".a"], [None,None,None,False])

#case = zip(["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"], ["","at","and","an","add","a",".at","bat",".at","an.","a.d.","b.","a.d","."], [None,None,None,None,None,False,False,None,True,True,False,False,True,False])

case = zip(["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"], ["","at","and","an","add",
    "a",".at","bat",".at","an.","a.d.","b.","a.d","."], [None,None,None,None,None,False,False,None,True,True,False,False,True,False])




wd = None
for op, param, expected in case:
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


