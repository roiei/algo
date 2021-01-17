import time
from util.util_list import *
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        cnt = 0
        for word in words:
            if len(set(word) - set(allowed)) == 0:
                cnt += 1

        return cnt


stime = time.time()
print(2 == Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print('elapse time: {} sec'.format(time.time() - stime))
