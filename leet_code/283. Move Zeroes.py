class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        num_zeros = nums.count(0)
        for i in range(num_zeros):
            nums.append(nums.pop(nums.index(0)))
        

stime = time.time()
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print('elapse time: {} sec'.format(time.time() - stime))