import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        
        #@lru_cache(None)
        def dfs(kinds, inc, start):
            if inc == n:
                return len(kinds)
        
            lengths = []
            for i in range(start, n):
                for j in range(i + 1, n + 1):
                    word = s[i:j]

                    if word in kinds:
                        continue

                    kinds.add(word)
                    lengths += dfs(kinds, inc + (j - i), j),
                    kinds.discard(word)

            return max(lengths) if lengths else 0
    
        res = dfs(set(), 0, 0)
        return res

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def dfs(start, seen):
            ans = 0
            if start == n:
                return ans

            for end in range(start + 1, n + 1):
                word = s[start:end]

                if word in seen:
                    continue

                seen.add(word)
                ans = max(ans, 1 + dfs(end, seen))
                seen.discard(word)

            return ans 
            
        return dfs(0, set())


stime = time.time()
print(5 == Solution().maxUniqueSplit("ababccc"))
print(2 == Solution().maxUniqueSplit("aba"))
print(1 == Solution().maxUniqueSplit("aa"))
print('elapse time: {} sec'.format(time.time() - stime))


# "  this   is  a sentence "

# 9/4 -> floating...
# 9/3 -> 3

# Input: text = "  walks  udp package   into  bar a"  11/5 = 2
# Output: "walks  udp  package  into  bar  a "