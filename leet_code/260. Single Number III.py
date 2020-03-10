

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        n = len(nums)
        freq = {}
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        return [k for k, v in freq.items() if v == 1]

#print(Solution().singleNumber([1,2,1,3,2,5]))
print(Solution().singleNumber([-1,0]))