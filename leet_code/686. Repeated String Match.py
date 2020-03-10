import time
from util_list import *
from util_tree import *


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n = len(A)
        m = len(B)
        l = max(n, m)
        cnt = 1
        s = A[:]
        while True:
            if len(s) > l*3:
                break

            print(s)
            if len(s) >= m:
                if -1 != s.find(B):
                    return cnt
            s += A
            cnt += 1
        return -1



stime = time.time()
print(Solution().repeatedStringMatch("abcd", "cdabcdab"))
#print(Solution().repeatedStringMatch("aa", "a"))
print(Solution().repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba"))
print('elapse time: {} sec'.format(time.time() - stime))

