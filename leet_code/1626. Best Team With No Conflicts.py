import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
You are the manager of a basketball team. 
For the upcoming tournament, 
you want to choose the team with the highest overall score. 
The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. 
A conflict exists if a younger player has a strictly higher score than an older player. 
A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] 
represents the score and age of the ith player, 
respectively, return the highest overall score of all possible basketball teams.

scores = [4,5,6,5], ages = [2,1,2,1]
         (4, 2), (5, 1), (6, 2), (5, 1)

         sort
         (6, 2) (5, 1) (5, 1) (4, 2)

 DP:      6   0   0   0
 i = 1    6   5
             mx(5, 5 + 6)
              11

 i = 2    6   11   5
         ---     ---
                 mx(6, 5 + 6)
                  11

          6   11   11
             --- ---
                 mx(11, 5 + 11)
                   16

 i = 3    6   11   16   4
         ---          ---
                     mx(4, 4 + 6)
          6   11   16   10
             ---      ----
                     mx(10, 4 + 5)
          6   11   16   10
                  ---  ----
                        X   <-- age is higher
          6   11   16   15
"""


class Solution:
    def bestTeamScore(self, scores: [int], ages: [int]) -> int:
        scores = sorted(list(zip(scores, ages)), reverse=True)
        n = len(scores)
        dp = [0]*n
        dp[0] = scores[0][0]

        for i in range(1, n):
            dp[i] = scores[i][0]

            for j in range(i):
                if scores[j][0] >= scores[i][0] and scores[j][1] >= scores[i][1]:
                    dp[i] = max(dp[i], dp[j] + scores[i][0])

        return max(dp)


stime = time.time()
print(34 == Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(16 == Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(6 == Solution().bestTeamScore([1,2,3,5], [8,9,10,1]))

print('elapse time: {} sec'.format(time.time() - stime))
