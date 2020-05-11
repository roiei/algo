
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def make_tuple(self, word):
        new_word = []
        for i in range(len(word)):
            new_word += (i, word[i]),

        return set(new_word)

    def buildDict(self, dict: [str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.words += self.make_tuple(word),

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        word_tuple = self.make_tuple(word)

        for w in self.words:
            diff_from = w - word_tuple
            diff_to = word_tuple - w
            if len(diff_from) == 1 and len(diff_to) == 1:
                return True

        return False

        
# params = list(zip(["MagicDictionary", "buildDict", "search", "search", "search", "search"],
# [[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]))
# exp_res = [None,None,True,True,False,False]

params = list(zip(["MagicDictionary", "buildDict", "search", "search", "search", "search"],
[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]))
exp_res = [None,None,False,True,False,False]



stime = time.time()
dic = None
res = []
for op, param in params:
    if op == 'MagicDictionary':
        dic = MagicDictionary()
        res += None,
    elif op == 'buildDict':
        res += dic.buildDict(param[0]),
    elif op == 'search':
        res += dic.search(param[0]),

print(res == exp_res)
print('elapse time: {} sec'.format(time.time() - stime))