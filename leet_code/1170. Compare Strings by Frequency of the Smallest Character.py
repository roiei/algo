
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(w):
            if not w:
                return 0
            freq = sorted(collections.Counter(w).items(), key=lambda p: p[0])
            return freq[0][1]
    
        res = []
        word_mxs = []
        
        for word in words:
            word_mxs += f(word),
        
        word_mxs.sort()
        
        for query in queries:
            query = f(query)
            idx = bisect.bisect_left(word_mxs, query)
            
            while idx < len(word_mxs):
                if query < word_mxs[idx]:
                    break
                idx += 1
            
            res += len(word_mxs[idx:]),
            
        return res
        

stime = time.time()
print([1,2] == Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
print('elapse time: {} sec'.format(time.time() - stime))