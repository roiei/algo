import time

class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int:
        mval = 0
        cnt = 0
        for i in range(len(nums)):
            if 1 == nums[i]:
                cnt += 1
            else:
                if cnt > mval:
                    mval = cnt
                cnt = 0
        if cnt > mval:
            mval = cnt
        return mval
        

stime = time.time()
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3
print('elapse time: {} sec'.format(time.time() - stime))