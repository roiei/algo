import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        dp = [0]*(target + 1)

        for didx in range(d):
            for 
    
        return dfs(target, d)

    int numRollsToTarget(int d, int f, int target) {
        vector<vector<int>> numWays(d+1, vector<int>(target+1, 0));
        for(int i=0; i<=d; i++)
        {
            for(int j=0; j<=target; j++)
            {
                if((i == 0) && (j == 0))
                    numWays[i][j] = 1;
                
                if((i == 0) || (j == 0))
                    continue;
                
                else
                {
                    for(int k=1; k<=f; k++)
                    {
                        if(j >= k) numWays[i][j]  = (numWays[i-1][j-k] + numWays[i][j]) % mod;
                    }
                }
            }
        }
        
        return numWays[d][target];
    }


stime = time.time()
print(1 == Solution().numRollsToTarget(d = 1, f = 6, target = 3))
print('elapse time: {} sec'.format(time.time() - stime))
