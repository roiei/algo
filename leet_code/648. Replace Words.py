import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        words = sentence.split()
        out = []
        
        for word in words:
            for d in dict:
                if True == word.startswith(d):
                    out += d,
                    break
            else:
                out += word,
    
        return ' '.join(out)


stime = time.time()
sol = Solution()
print("the cat was rat by the bat" == sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
print('elapse time: {} sec'.format(time.time() - stime))
#576