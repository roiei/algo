import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = collections.Counter(sentence)
        
        for i in range(26):
            letter = chr(ord('a') + i)
            if freq[letter] == 0:
                return False
        
        return True


print(True == Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(False == Solution().checkIfPangram("leetcode"))