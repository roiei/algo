
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        each = n//4
        cnt = collections.defaultdict(int)

        for ch in 'QWER':
            cnt[ch] = 0

        for ch in s:
            cnt[ch] += 1

        print('n = {}, each = {}, cnt = {}'.format(n, each, cnt))
        need = over = 0

        for k, v in cnt.items():
            if v < each:
                need += each - v
            else:
                over += v - each

            print('over = {}, need = {}'.format(over, need))


        print(need, over)
        return need if need == over else 0

    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res


    def balancedString(self, s: str) -> int:
        cntr = collections.Counter(s)
        res = n = len(s)
        need = len(s)//4
        
        j = 0
        i = 0
        
        while i < n:
            cntr[s[i]] -= 1
            i += 1
            
            while j < n:
                if any(cntr[ch] > need for ch in 'QWER'):
                    break
                    
                res = min(res, i - j)
                cntr[s[j]] += 1
                j += 1
            
        return res









stime = time.time()
#print(["/a","/c/d","/c/f"] == Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
#print(0 == Solution().balancedString("QWER"))
# print(1 == Solution().balancedString("QQWE"))
# print(2 == Solution().balancedString("QQQW"))
# print(3 == Solution().balancedString("QQQQ"))
print(4 == Solution().balancedString("WWEQERQWQWWRWWERQWEQ"))
print('elapse time: {} sec'.format(time.time() - stime))