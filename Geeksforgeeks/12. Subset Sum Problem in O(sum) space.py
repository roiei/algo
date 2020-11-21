
import collections


def canPartitionKSubsets(self, nums, k):
    if not nums or not k or 0 != sum(nums)%k:
        return False

    def dfs(nums, n, k, start, used, part, inc):
        if k == 1:
            return True
        if inc > part:
            return False
        if inc == part:
            inc = 0
            k -= 1
            start = 0

        for i in range(start, n):
            if used[i] == True:
                continue
            used[i] = True
            if dfs(nums, n, k, i+1, used, part, inc + nums[i]):
                return True
            used[i] = False
        return False

    used = [False]*len(nums)
    return dfs(nums, len(nums), k, 0, used, sum(nums)//k, 0)


tc = int(input())
for t in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))
    if 0 == sum(nums)%2 and True == canPartitionKSubsets(nums, 2):
        print('YES')
    else:
        print('NO')



print(is_subset_sum([4, 1, 10, 12, 5, 2], 6, 9))
print(isSubsetSum([4, 1, 10, 12, 5, 2], 6, 9))





