
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


stime = time.time()
print("Hello how are you" == Solution().evaluate(s = "Hello how are you Contestant", k = 4))
print('elapse time: {} sec'.format(time.time() - stime))