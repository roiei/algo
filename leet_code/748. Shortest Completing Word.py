import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def find_substr(self, s, ss):
        m = len(s)
        n = len(ss)
        j = 0
        for i in range(m):
            if ss[j] == s[i]:
                j += 1
            if j == n:
                return True
        return False

    def shortestCompletingWord(self, licensePlate: str, words: [str]) -> str:
        if '' == licensePlate:
            return ''
        lp = licensePlate.replace(' ', '')
        lp = [letter for letter in lp.lower() if 'a' <= letter <= 'z']
        lp = ''.join(sorted(lp))
        valid = []
        for word in words:
            sword = ''.join(sorted(word.lower()))
            if True == self.find_substr(sword, lp):
                valid += (word, len(word)),
        valid.sort(key=lambda p:p[1], reverse=False)
        return valid[0][0] if valid else ''

    def shortestCompletingWord(self, licensePlate: str, words: [str]) -> str:
        lp = ''.join(sorted([ch.lower() for ch in licensePlate if ch.isalpha()]))
        m = len(lp)
        res = []
        mn = float('inf')

        for word in words:
            sword = ''.join(sorted([ch.lower() for ch in word]))
            n = len(sword)
            i = j = 0

            while i < m and j < n:
                if lp[i] == sword[j]:
                    i += 1
                j += 1

            if i == m:
                if mn > len(sword):
                    res = [word]
                    mn = len(word)
                elif mn == len(sword):
                    res += word,
 
        return res[0] if res else ''


stime = time.time()
#print("husband" == Solution().shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))
#print(Solution().shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))
#print('pest' == Solution().shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))
#print(Solution().shortestCompletingWord("TE73696", ["ten","two","better","talk","suddenly","stand","protect","collection","about","southern"]))
print('elapse time: {} sec'.format(time.time() - stime))