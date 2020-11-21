import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        
        while s:
            ns = []
            pre_s = s[:]
            ch1 = s.pop(0)
            if not s:
                s += ch1,
                break
            
            while s:
                ch2 = s.pop(0)
                if ch1.lower() == ch2.lower() and ch1 != ch2:
                    if not s:
                        break

                    ch1 = s.pop(0)
                    if not s:
                        ns += ch1,
                        break

                    continue

                ns += ch1,
                ch1 = ch2

                if not s:
                    ns += ch2,

            s = ns
            if pre_s == ns:
                break

        return ''.join(s)


stime = time.time()
#print("leetcode" == Solution().makeGood("leEeetcode"))
#print("" == Solution().makeGood("abBAcC"))
print("" == Solution().makeGood("RLlr"))
print('elapse time: {} sec'.format(time.time() - stime))