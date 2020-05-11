
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def camelMatch(self, queries: [str], pattern: str) -> [bool]:
        pat = []
        i = 0

        while i < len(pattern):
            # skip lower
            while i < len(pattern) and pattern[i].islower():
                i += 1

            p = i
            if i < len(pattern) and pattern[i].isupper():
                i += 1

            while i < len(pattern) and pattern[i].islower():
                i += 1

            if i - p > 0:
                pat += pattern[p:i],

        res = []

        for query in queries:
            chunks = []
            i = 0

            while i < len(query):
                #skip lower
                while i < len(query) and query[i].islower():
                    i += 1

                if i >= len(query):
                    break

                p = i
                i += 1 # skip first upper

                while i < len(query) and query[i].islower():
                    i += 1

                chunks += query[p:i],

            if len(pat) != len(chunks):
                res += False,
                continue

            for i in range(len(pat)):
                j = 0
                k = 0

                while j < len(pat[i]) and k < len(chunks[i]) and pat[i][j].isupper() and chunks[i][k].isupper():
                    j += 1
                    k += 1

                while j < len(pat[i]) and k < len(chunks[i]):
                    if pat[i][j] == chunks[i][k]:
                        j += 1

                    k += 1

                if j != len(pat[i]):
                    break
            else:
                res += True,
                continue

            res += False,

        return res
        

stime = time.time()
print([True,False,True,True,False] == Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
print([True,False,True,False,False] == Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
print([False,False,True] == Solution().camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP"))
print('elapse time: {} sec'.format(time.time() - stime))