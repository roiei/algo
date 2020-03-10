import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def letterCasePermutation(self, S: str) -> [str]:
        letters = []
        S = S.lower()
        
        for ch in S:
            if 'a' <= ch <= 'z':
                letters += (ch, ch.upper()),
                
        def dfs(letters, start, perm, perms, skip):
            if len(perm) == len(letters):
                perms += perm[:],
                return
        
            for i in range(len(letters[start])):
                if (start, i) in skip:
                    continue
                skip += (start, i),
                perm += letters[start][i],
                dfs(letters, start + 1, perm, perms, skip)
                perm.pop()
                skip.pop()
        
        perms = []
        dfs(letters, 0, [], perms, [])

        out = []
        for perm in perms:
            word = []
            i = 0
            for ch in S:
                if 'a' <= ch <= 'z':
                    word += perm[i],
                    i += 1
                else:
                    word += ch,
            out += ''.join(word),
        
        return out


stime = time.time()
print(["rmr","rmR","rMr","rMR","Rmr","RmR","RMr","RMR"] == Solution().letterCasePermutation("RmR"))
print('elapse time: {} sec'.format(time.time() - stime))