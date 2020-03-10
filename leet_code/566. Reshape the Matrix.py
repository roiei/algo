
class Solution:
    def matrixReshape(self, nums: 'List[List[int]]', r: int, c: int) -> 'List[List[int]]':
        sr = len(nums)
        sc = len(nums[0])
        if sr*sc != r*c:
            return nums
        oned = []
        for num in nums:
            oned.extend(num)
        res = []
        for y in range(r):
            res.append(oned[y*c:y*c+c])
        return res
