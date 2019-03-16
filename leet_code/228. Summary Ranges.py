class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        if not nums:
            return []

        i = 0
        res = []
        while i < len(nums):
            j = i+1
            cur_val = nums[i]
            start = end = i

            while j < len(nums):
                if cur_val+1 == nums[j]:
                    end+= 1
                    cur_val += 1
                else:
                    break
                j+= 1

            res.append([start, end])
            i+= end-start + 1

        ret = []
        for r in res:
            if nums[r[0]] == nums[r[1]]:
                ret.append("{}".format(nums[r[0]]))
            else:
                ret.append('{}->{}'.format(nums[r[0]], nums[r[1]]))
        return ret

nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]

sol = Solution()
ret = sol.summaryRanges(nums)
print(ret)

