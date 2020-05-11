
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        dic = {order[i]:i for i in range(len(order))}
        word_info = []
        
        for word in words:
            word_seq = []
            for i in range(len(word)):
                word_seq += dic[word[i]],
            
            word_info += (word, word_seq),

        word_info.sort(key=lambda p: p[1])
        
        for i in range(len(words)):
            if words[i] != word_info[i][0]:
                break
        else:
            return True
        
        return False

    def isAlienSorted(self, words: [str], order: str) -> bool:
        dic = {order[i]:i for i in range(len(order))}
        word_info = [(word, [dic[word[i]] for i in range(len(word))]) for word in words]
        
        word_info.sort(key=lambda p: p[1])
        
        for i in range(len(words)):
            if words[i] != word_info[i][0]:
                break
        else:
            return True
        
        return False
        

stime = time.time()
print(True == Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print('elapse time: {} sec'.format(time.time() - stime))