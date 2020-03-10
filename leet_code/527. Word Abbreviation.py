
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        n = len(dict)
        pre = [1]*n

        def abbreviate(s, k):
            length = len(s)
            if length - 2 <= k:
                return s
            return s[0:k] + str(length - k - 1) + s[-1]

        res = []
        for i in range(n):
            res += abbreviate(dict[i], pre[i]),

        for i in range(n):
            while True:
                st = set()
                for j in range(i + 1, n):
                    if res[j] == res[i]:
                        st.add(j)

                if not st:
                    break

                st.add(i)
                for si in st:
                    pre[si] += 1
                    res[si] = abbreviate(dict[si], pre[si])

        return res




stime = time.time()
#print(Solution().wordsAbbreviation(["intension","intrusion", "z"]))
print(["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"] == Solution().wordsAbbreviation(["like","god","internal","me","internet","interval","intension","face","intrusion"]))

#print(["w3e","t3e","is","b7l","way"] == Solution().wordsAbbreviation(["where","there","is","beautiful","way"]))
print('elapse time: {} sec'.format(time.time() - stime))