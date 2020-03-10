import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            p = {}
            used = []
            for i, ch in enumerate(pattern):
                if ch not in p and word[i] not in used:
                    p[ch] = word[i]
                    used += word[i],
                    continue
                elif ch not in p:
                    break
                
                if p[ch] != word[i]:
                    break
            else:
                res += word,
        
        return res


stime = time.time()

print("blue is sky the" == Solution().reverseWords("the sky is blue"))
print('elapse time: {} sec'.format(time.time() - stime))