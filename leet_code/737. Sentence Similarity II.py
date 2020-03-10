
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    """
    @param words1: 
    @param words2: 
    @param pairs: 
    @return: Whether sentences are similary or not?
    """
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        g = collections.defaultdict(dict)
        
        for u, v in pairs:
            g[u][v] = True
            g[v][u] = True
        
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            
            found = False
            q = [words1[i]]
            
            #visited = set(words1[i])  # DO NOT LIKE THIS ! IT MAKES WRONG RESULT !
            visited = set()
            visited.add(words1[i])
            
            while q:
                u = q.pop(0)
                if u == words2[i]:
                    found = True
                    break
                for v, link in g[u].items():
                    if v in visited:
                        continue
                    visited.add(v)
                    q += v,
            
            if found == False:
                return False
        
        return True


stime = time.time()
#print(True == Solution().areSentencesSimilarTwo(["great","acting","skills"], ["fine","drama","talent"], [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))

print(True == Solution().areSentencesSimilarTwo(
    ["7", "5", "4", "11", "13", "15", "19", "12", "0", "10"],
    ["16", "1", "7", "3", "15", "10", "13", "2", "19", "8"],

[["6", "18"], ["8", "17"], ["1", "13"], ["0", "8"], ["9", "14"], ["11", "17"], ["11", "19"], ["13", "16"], ["0", "18"], ["3", "11"], ["1", "9"], ["2", "11"], ["2", "4"], ["0", "19"], ["8", "12"], ["8", "19"], ["16", "19"], ["1", "11"], ["2", "18"], ["0", "16"], ["7", "11"], ["6", "8"], ["9", "17"], ["8", "16"], ["3", "13"], ["7", "9"], ["7", "10"], ["3", "6"], ["15", "19"], ["1", "5"], ["2", "14"], ["1", "18"], ["8", "15"], ["14", "19"], ["3", "17"], ["6", "10"], ["5", "17"], ["10", "15"], ["1", "10"], ["4", "6"]]))
print('elapse time: {} sec'.format(time.time() - stime))