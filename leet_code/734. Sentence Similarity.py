
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        adict = collections.defaultdict(list)
        
        if len(words1) != len(words2):
            return False
    
        for u, v in pairs:
            adict[u] += v,
            adict[v] += u,
        
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words2[i] in adict[words1[i]]:
                continue
            
            return False
        
        return True


stime = time.time()
print(True == Solution().isSentenceSimilarity(words1=["great","acting","skills"], words2=["fine","drama","talent"], pairs=[["great","fine"],["drama","acting"],["skills","talent"]]))
print('elapse time: {} sec'.format(time.time() - stime))