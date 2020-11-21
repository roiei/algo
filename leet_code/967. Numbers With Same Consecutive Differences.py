import time
import copy
import collections


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def dfs(n, depth, nums, res):
            
            if n == depth:
                if len(nums) > 1 and nums[0] == 0:
                    return
                res += int(''.join(map(str, nums))),
                return
        
            for i in range(10):
                if abs(nums[-1] - i) != K:
                    continue
                
                nums += i,
                dfs(n, depth + 1, nums, res)
                nums.pop()
            
        
        res = []
        nums = []
        for i in range(10):
            nums += i,
            dfs(N - 1, 0, nums, res)
            nums.pop()
        
        return res

    def numsSameConsecDiff(self, N, K):
        def dfs(depth, seq, res):
            if depth == N:
                if len(seq) > 1 and seq[0] == 0:
                    return
                res.add(int(''.join(map(str, seq))))
                return

            for i in range(10):
                if not seq or (seq and abs(i - seq[depth - 1]) == K):
                    dfs(depth + 1, seq + [i], res)

        res = set()
        dfs(0, [], res)
        print(list(res))
        return list(res)


stime = time.time()
print([181,292,707,818,929] == Solution().numsSameConsecDiff(N = 3, K = 7))
#print(Solution().numsSameConsecDiff(1, 0))
print('elapse time: {} sec'.format(time.time() - stime))