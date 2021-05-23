import time
import copy
import heapq
import collections
from typing import List


# 5763. Longer Contiguous Segments of Ones than Zeros
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mo = mz = 0
        ones = zeros = 0
        if len(s) == 1:
            ones = 1 if s[0] == '1' else 0
            zeros = 1 if s[0] == '0' else 0
            mo = max(mo, ones)
            mz = max(mz, zeros)
            return mo > mz

        for i in range(1, len(s)):
            if s[i] == '1' and ones == 0:
                ones = 1
                zeros = 0
            elif s[i] == '0' and zeros == 0:
                zeros = 1
                ones = 0

            if s[i] == '1' and s[i - 1] == s[i]:
                ones += 1
            elif s[i] == '0' and s[i - 1] == s[i]:
                zeros += 1

            mo = max(mo, ones)
            mz = max(mz, zeros)

        return mo > mz


#stime = time.time()
#print(True == Solution().checkZeroOnes("1101"))
# print(True == Solution().checkZeroOnes("1"))
# #print(False == Solution().checkZeroOnes("100110"))
# print('elapse time: {} sec'.format(time.time() - stime))


#5764. Minimum Speed to Arrive on Time
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        

stime = time.time()
print(1 == Solution().minSpeedOnTime(dist = [1,3,2], hour = 6))
print('elapse time: {} sec'.format(time.time() - stime))