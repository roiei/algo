
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    # timeout
    def findNumOfValidWords(self, words, puzzles):
        puzz_set = []
        for puzzle in puzzles:
            temp = set()
            puzz_set += set(puzzle),
            
        word_set = []
        for word in words:
            word_set += set(word),
        
        n = len(puzzles)
        res = []
        
        for i in range(n):
            cnt = 0
            for j in range(len(words)):
                if puzzles[i][0] in words[j] and word_set[j] == (puzz_set[i] & word_set[j]):
                    cnt += 1
            res += cnt,
        
        return res



stime = time.time()
#print([1,1,3,2,4,0] == Solution().findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
print([0,1,3,2,0] == Solution().findNumOfValidWords(["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))
print('elapse time: {} sec'.format(time.time() - stime))