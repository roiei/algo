import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]


class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # 1  3  4  7 <- update distance if the two adjacent items are differnt word
        # --   ---

        tgt_words = {word1, word2}
        positions = []
        mn = float('inf')

        for i, word in enumerate(words):
            if word in tgt_words:
                positions += (i, word),

        for i in range(1, len(positions)):
            if positions[i][1] != positions[i - 1][1]:
                mn = min(mn, positions[i][0] - positions[i - 1][0])

        return mn


stime = time.time()
print(3 == Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
print(1 == Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","coding"))
print('elapse time: {} sec'.format(time.time() - stime))
