import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
        ]
        
        res = []
        for word in words:
            lower_word = word.lower()
            keyline = None
            for row in keyboard:
                if lower_word[0] in row:
                    keyline = row
                    break
            
            if keyline == None:
                continue
            
            for ch in lower_word:
                if ch not in keyline:
                    break
            else:
                res += word,
        
        return res


stime = time.time()
sol = Solution()
print(["Alaska", "Dad"] == sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print('elapse time: {} sec'.format(time.time() - stime))
