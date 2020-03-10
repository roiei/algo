
import time

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        preCap = True
        num_caps = 0
        for s in word:
            if 'A' <= s <= 'Z':
                if True != preCap:
                    return False
                num_caps += 1
            else:
                if True == preCap:
                    preCap = False
        if num_caps > 1 and num_caps != len(word):
            return False
        return True


stime = time.time()
print(Solution().detectCapitalUse('USA'))
print(Solution().detectCapitalUse('FlaG'))
print(Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))
print('elapse time: {} sec'.format(time.time() - stime))