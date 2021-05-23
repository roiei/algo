import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0

        for type, color, name in items:
            if ruleKey == 'type':
                if ruleValue == type:
                    cnt += 1
            elif ruleKey == 'color':
                if ruleValue == color:
                    cnt += 1
            elif ruleKey == 'name':
                if ruleValue == name:
                    cnt += 1

        return cnt


stime = time.time()
print(1 == Solution().countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
print('elapse time: {} sec'.format(time.time() - stime))