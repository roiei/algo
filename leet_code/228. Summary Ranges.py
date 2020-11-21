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
            i+= end - start + 1

        ret = []
        for r in res:
            if nums[r[0]] == nums[r[1]]:
                ret.append("{}".format(nums[r[0]]))
            else:
                ret.append('{}->{}'.format(nums[r[0]], nums[r[1]]))
        return ret

    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return []
        res = []
        
        def add_range(start, end, res):
            if start == end:
                res += '{}'.format(start),
            else:
                res += '{}->{}'.format(start, pre),
                
        pre = start = nums[0]
        for i in range(1, len(nums)):
            if pre + 1 < nums[i]:
                add_range(start, pre, res)
                start = nums[i]
            pre = nums[i]
        
        add_range(start, pre, res)        
        return res

    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return None

        n = len(nums)
        start = end = nums[0]
        res = []

        def get_range(start, end):
            return '{}'.format(start) if start == end else '{}->{}'.format(start, end)

        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                end = nums[i]
                continue
            else:
                res += get_range(start, end),
                start = end = nums[i]

        res += get_range(start, end),
        return res


print(['0->2', '4->5', '7'] == Solution().summaryRanges([0,1,2,4,5,7]))
print(['0', '2->4', '6', '8->9'] == Solution().summaryRanges([0,2,3,4,6,8,9]))

