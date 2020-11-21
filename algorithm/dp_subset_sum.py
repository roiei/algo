


nums = [34, 4, 12, 5, 2]
target = 9
#target = 40


def dfs(nums, depth, n, target):
    if target == 0:
        return True
    if depth == n or target < 0:
        return False

    res = dfs(nums, depth + 1, n, target - nums[depth]),
    res += dfs(nums, depth + 1, n, target),
    return any(res)


mem = {}
def dfs_dp(nums, depth, n, target):
    if depth in mem:
        return mem[depth]
    if target == 0:
        return True
    if depth == n or target < 0:
        return False

    res = dfs(nums, depth+1, n, target - nums[depth]),
    res += dfs(nums, depth+1, n, target),
    mem[depth] = any(res)
    return mem[depth]


def isSubsetSum(nums, n, target): 
    subset = ([[False for i in range(target+1)] for i in range(n+1)]) 
    for i in range(n+1): 
        subset[i][0] = True
        for i in range(1, target+1): 
            subset[0][i] = False
              
        for i in range(1, n+1): 
            for j in range(1, target+1):
                if j < nums[i-1]: 
                    subset[i][j] = subset[i-1][j] 
                else:
                    subset[i][j] = (subset[i-1][j] or 
                                   subset[i-1][j-nums[i-1]])
      
    return subset[n][target] 


def is_subset_sum(nums, n, target):
    dp = [False]*(target+1)
    cmb = [True]*(target+1)
    for num in nums:
        if num <= target:
            print(f'num = {num}')
            dp[num] = True
            cmb[num] = False
        for i in range(1, target+1):
            if dp[i] == True and (i+num <= target):
                if i != num and cmb[i] == False:
                    dp[i+num] = True
    return dp[target]



# print(dfs(nums, 0, len(nums), target))
# print(dfs_dp(nums, 0, len(nums), target))
print(isSubsetSum(nums, len(nums), target))
print(is_subset_sum(nums, len(nums), target))
