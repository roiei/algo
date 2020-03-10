
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def spellchecker(self, wordlist: [str], queries: [str]) -> [str]:

        words_unique = set(wordlist)
        words_cap = {}
        words_ast = {}

        for word in wordlist:
            word_low = word.lower()
            # words_cap.setdefault(wordlow, word)
            # words_ast.setdefault(devowel(wordlow), word)

            if word_low not in words_cap:
                words_cap[word_low] = word

            word_ast = ''.join('*' if ch in 'aeiou' else ch for ch in word_low)
            if word_ast not in words_ast:
                words_ast[word_ast] = word


        def solve(query):
            if query in words_unique:
                return query

            #words_cap.get(query.lower)

            lower = query.lower()
            if lower in words_cap:
                return words_cap[lower]

            low_asteric = ''.join('*' if ch in 'aeiou' else ch for ch in lower)
            if low_asteric in words_ast:
                return words_ast[low_asteric]
            
            return ''

        res = []
        for query in queries:
            res += solve(query),
        return res

        #return map(solve, queries)
    

stime = time.time()
print(["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"] == Solution().spellchecker(
    wordlist = ["KiTe","kite","hare","Hare"], 
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
print('elapse time: {} sec'.format(time.time() - stime))