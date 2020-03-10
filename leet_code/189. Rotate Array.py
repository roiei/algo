class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if k > n:
            k = k%n
        if n <= 1:
            return
        if n == k:
            return
        move = nums[n-k:]
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(len(move)):
            nums[i] = move[i]

