import time
import bisect
import collections


class Solution:
    def get_range_cases(self, nums, s, e, lower, upper, res):
        cnt = 0
        if s > e:
            return cnt
        print('{}, {}'.format(s, e))
        idx = '{}:{}'.format(s, e)
        if idx in res:
            return 0
        tot = sum(nums[s:e+1])
        if lower <= tot <= upper:
            if idx not in res:
                cnt += 1
        cnt += self.get_range_cases(nums, s+1, e, lower, upper, res)
        cnt += self.get_range_cases(nums, s, e-1, lower, upper, res)
        if idx not in res:
            res[idx] = cnt
        return cnt

    def get_range_cases_stk(self, nums, s, e, lower, upper, res):
        stk = [[s, e]]
        cnt = 0
        while stk:
            nstk = []
            while stk:
                s, e = stk.pop()
                if s > e:
                    continue
                idx = '{}:{}'.format(s, e)
                if idx in res:
                    continue
                tot = sum(nums[s:e+1])
                if lower <= tot <= upper:
                    if idx not in res:
                        cnt += 1
                nstk.append([s+1, e])
                nstk.append([s, e-1])
                if idx not in res:
                    res[idx] = cnt
            stk = nstk
        return cnt

    def countRangeSum2(self, nums: 'List[int]', lower: int, upper: int) -> int:
        if not nums:
            return 0
        res = {}
        return self.get_range_cases_stk(nums, 0, len(nums)-1, lower, upper, res)

    def countRangeSum(self, nums, lower, upper):
        sums, sm, res = [0], 0, 0
        for num in nums:
            sm += num
            print('sm - lower = ', sm - lower, ', ' , bisect.bisect_right(sums, sm - lower))
            print('sm - upper = ', sm - upper, ', ', bisect.bisect_left(sums, sm - upper))
            res += bisect.bisect_right(sums, sm - lower) - bisect.bisect_left(sums, sm - upper)
            bisect.insort(sums, sm)
        return res

    def countRangeSum(self, nums, lower, upper):
        cs, out = 0, 0
        m = collections.defaultdict(int)

        for i in range(len(nums)):
            cs += nums[i]
            if lower <= cs <= upper:
                out += 1
            for x in range(lower, upper + 1):
                if cs - x in m:
                    out += m[cs - x]

            m[cs] += 1
        print(m)
        return out

    def countRangeSum(self, nums, lower, upper):
        
        def dfs(l, r, tot):
            if l > r:
                return 0
            
            if (l, r) in mem:
                return 0
        
            cnt = 0
            
            if lower <= tot <= upper:
                print(l, r)
                cnt += 1
            
            cnt += dfs(l + 1, r, tot - nums[l])
            cnt += dfs(l, r - 1, tot - nums[r])
            
            mem[(l, r)] = cnt
            return cnt
    
        mem = {}
        cnt = dfs(0, len(nums) - 1, sum(nums))
        return cnt

    def countRangeSum(self, nums, lower, upper):
        dp = collections.defaultdict(int)
        tot = 0
        cnt = 0
        for num in nums:
            tot += num
            if lower <= tot <= upper:
                cnt += 1

            for k in dp:
                if lower <= tot - k <= upper:
                    cnt += dp[k]

            dp[tot] += 1

        return cnt


stime = time.time()
print(3 == Solution().countRangeSum([-2,5,-1], -2, 2))
print(4 == Solution().countRangeSum([2147483647,-2147483648,-1,0], -1, 0))

#print(Solution().countRangeSum([2147483647,-2147483648,-1,0], -1, 0)) # 4
#print(Solution().countRangeSum([13,6,13,4,27,-14,-13,15,-4,13,-15,21,-23,19,3,-14,-27,-17,-4,15,1,-27,-17,-12,-26,12,11,-24,9,-18,18,26,-5,-25,-29,-26,17,-24,-22,27,-2,16,-7,-17,15,-10,-24,-14,-19,-22,-1,-9,-30,-11,20,-14,-5,4,20,7,-2,20,26,16,-13,-10,3,-29,13,26,14,-2,-13,18,28,9,-11,17,-28,-4,-23,-23,-7,-22,11,2,-24,-4,-11,9,-23,29,9,-10,-17,-16,-11,2,-28,3,12,-8,-16,-16,-25,27,21,-17,-5,17,-17,-30,2,-13,-14,-2,-15,-26,-12,9,12,-26,19,21,10,-10,9,-15,5,-1,-14,19,-18,-30,15,-9,-19,-11,-20,14,-9,18,-19,-9,-18,29,14,-29,11,-9,-7,-21,12,-17,-11,-23,-8,1,-1,-5,-22,-26,-18,27,6,-24,-27,21,-25,-22,17,18,28,20,-7,19,6,-11,14,10,6,-22,-4,13,5,5,3,-10,0,-6,-29,2,-22,10,-26,3,-23,29,28,4,0,-26,13,-1,4,-13,25,23,27,-30,5,-21,26,-12,4,4,23,4,-27,15,5,15,11,-1,0,-28,8,-26,-22,27,-3,6,-19,-28,27,8,-13,-30,3,25,-9,2,-5,26,-2,7,11,-22,26,-6,8,22,24,7,8,8,28,-22,-12,5,-2,1,-8,-30,-20,4,-17,22,-6,-25,-4,27,20,25,8,14,-26,20,3,1,18,-27,3,4,-20,9,-30,3,-26,-21,0,-24,-20,-18,-28,-28,-18,-25,-14,-3,-15,25,3,-16,-24,-13,13,-12,27,-26,9,15,23,17,-14,-20,-2,15,0,3,6,9,26,18,-11,27,19,16,3,9,7,-12,15,7,26,28,1,-3,-19,27,-27,-29,8,22,9,-15,-3,-17,25,15,-16,20,-28,28,22,28,16,-27,-21,-17,-17,24,-10,-16,-27,-18,-25,-13,25,11,28,-7,7,6,23,-27,-19,13,25,-23,-14,-21,4,-10,0,-24,26,5,-6,6,-27,23,-30,10,19,-12,10,15,-5,-15,-2,7,-1,-17,-14,10,29,-24,-7,2,21,-19,-8,-27,-3,22,-5,-6,8,26,10,-17,12,-6,9,3,7,-26,-26,4,6,2,23,7,13,-20,-19,5,3,0,-10,-21,25,-20,-20,-22,6,-18,19,22,-13,-21,17,4,-22,19,6,5,25,-17,6,18,19,11,23,3,6,22,24,-15,-27,-5,-12,-27,14,-22,26,-26,-11,-20,-7,18,19,23,-25,17,-27,22,22,-13,-23,-6,-18,25,7,-13,-24,-6,-1,18,13,-12,3,11,-20,10,-13,18,25,-7,-8,-17,17,-3,5,16,23,17,-18,27,26,-10,20,5,-11,5,-29,18,29,12,2,-21,-11,-4,12,-5,24,5,-20,25,9,3,-8,2,19,20,24,-1,-3,-2,-27,19,24,28,13,17,16,13,-12,-8,5,-14,21,-2,-25,6,9,-13,1,-12,26,-13,15,-21,13,4,16,5,-24,15,-14,15,14,-28,21,1,-8,21,-25,-5,-23,-15,-18,-25,-24,7,25,-18,-22,15,4,-25,-17,-9,-1,15,6,26,22,15,17,-22,-2,15,-28,-16,-14,-20,17,-18,-4,6,17,-19,7,0,-3,-26,15,12,-5,-25,-21,26,17,14,-28,13,13,29,2,7,-12,1,28,-1,-20,-30,-15,5,25,-20,-18,-15,-25,-23,24,16,-2,-26,-22,16,-20,-5,-20,18,-28,-24,7,-17,-12,-22,17,29,-8,11,25,-4,-26,-18,20,-23,-29,27,27,17,20,7,-11,-9,-26,-5,5,-6,-16,-4,13,11,-6,-20,19,-9,8,12,-15,3,25,-23,0,-24,6,-24,-23,-1,-5,22,-29,7,-20,-7,18,-18,-18,15,17,-7,-12,29,-12,-28,-11,-25,28,19,-16,-25,23,-25,8,-13,-18,-28,-17,-15,6,-5,-27,18,15,-11,-30,6,23,8,-4,4,-14,-29,12,18,11,1,12,4,24,5,-14,-29,-4,-11,4,16,-30,-16,23,-21,-19,6,26,22,19,-8,27,-14,-8,-6,-30,-26,27,-26,-28,-25,8,10,-4,-15,0,22,-20,-20,10,-17,-11,13,9,8,24,-16,-16,-8,25,3,22,-8,24,-6,9,-29,20,-9,24,-8,23,-8,22,-4,15,0,19,10,27,26,23,20,15,18,-22,4,-18,-18,-30,7,-21,5,-12,25,-9,-4,-30,-4,20,-19,22,3,18,17,8,-13,-17,9,7,25,11,-10,-27,-3,-17,10,-30,-24,-29,-21,-2,-3,2,-25,26,-9,-12,18,-17,15,20,9,21,-24,5,7,-28,18,8,-11,16,-26,3,3,6,-16,-12,18,4,-17,-19,10,22,-6,20,6,28,2,-15,7,-20,11,3,-22,-20,-25,28,5,-11,-23,20,16,23,-5,5,8,-23,25,6,26,-7,-13,-2,-8,29,17,20,-14,-15,17,-20,-14,-27,21,29,-11,-20,8,19,-18,-1,29,5,14,23,15,7,11,-15,15,10,9,16,26,-8,-29,7,6,-9,-30,-6,18,-2,-10,18,-29,-1,-23,24,23,-15,-4,-3,-19,22,18,-27,-11,14,8,4,-6,10,-12,-10,21,7,-15,-21,2,12,3,-30,-9,-25,8,19,5,12,-12,-15,-12,-9,19,-7,17,0,5,17,-1,22,13,-27,15,-28,-29,23,-19,13,-8,23,12,-13,-15,-18,-26,-22,-3,-7,2,-4,24,2,11,21,-27,26,14,13,14,-30,19,-22,-29,-1,-27,-4,25,-14,-12,4,-6,-18,-11,-8,-5,29,9,-11,22,-10,10,-8,5,12,-21,27,-1,28,-21,15,26,-16,10,-17,7,-24,0,-20,-13,3,15,-19,-18,-8,-12,20,10,-8,25,26,-11,23,14,-1,-7,-22,-22,-16,-2,19,-27,5,17,28,20,17,-12,-13,-7,22,17,-8,-2,28,5,29,-27,-15,-2,26,-30,-6,-4,16,25,5,-19,1,-14,-6,29,-13,27,20,7,10,21,12,10,-12,-21,-10,-2,-18,-11,-15,1,-11,21,6,26,20,-24,29,6,26,-5,-18,-12,-16,-11,11,-24,4,13,15,-9,-3,17,-16,5,-17,-25,-30,-21,15,-16,27,-5,-4,-25,28,7,17,27,-18,-20,-9,13,3,-12,-16,-23,19,-9,10,0,-22,-23,10,-20,-4,25,28,-8,-20,7,-1,-26,-12,8,-22,24,21,-15,-26,-5,10,24,-27,-5,-1,-30,29,23,28,-10,-27,-16,13,-1,12,-10,13,14,-30,-5,-25,19,-19,13,26,27,3,3,28,3,-9,8,6,23,-2,-9,-26,22,-2,19,12,-19,-15,15,9,-29,-24,27,-1,-15,-17,11,11,-1,14,-29,-19,24,-29,-4,-15,-26,-21,9,-1,-22,-17,-9,-28,-1,-29,9,25,13,14,-29,-23,-22,1,-14,26,-27,-14,12,13,11,1,14,-1,11,-14,-16,-3,5,2,-8,-12,0,17,-5,-6,-6,25,-19,21,25,12,4,21,-9,8,-11,-30,26,19,15,20,18,-13,0,-30,8,-16,-2,-17,2,17,-21,-25,5,26,26,23,-6,-28,11,-16,1,-5,13,-14,7,0,-10,-30,-16,-29,-25,12,-15,-9,-2,15,4,-18,27,19,-26,4,-17,18,-15,-24,24,-17,-16,19,-30,-20,13,20,18,-14,-26,-22,10,23,27,-28,5,-6,-21,26,-3,10,1,26,-18,9,16,-6,13,-29,8,6,-30,-1,20,-30,0,23,1,-23,20,-25,-29,29,29,21,-13,-5,3,-16,-18,24,7,27,-27,-11,-21,14,10,0,15,26,-9,23,-13,-6,22,-9,-9,-6,-7,-25,6,-7,19,22,-24,28,29,4,16,28,23,0,-3,21,-1,3,-25,-19,-19,17,-22,9,28,-11,28,-4,-3,-25,21,-23,-30,10,25,-18,10,17,-15,27,19,3,18,-30,29,6,-26,10,27,21,1,-26,-20,-10,-6,26,-3,-13,0,-2,22,4,-28,-8,-26,-29,8,-12,-13,29,4,3,3,-12,-7,28,26,-29,28,-20,-15,-19,26,26,-27,14,-5,-6,21,-28,15,-30,-20,-26,-7,-26,27,24,-9,-10,-21,26,-5,-16,0,23,-3,-20,-5,15,-10,-4,-2,16,17,-17,-3,-22,-27,25,28,-26,-6,-14,-8,-19,-24,-8,12,-26,-13,-7,10,29,-7,-10,-30,13,15,21,-1,5,7,1,8,7,-2,-13,15,-19,15,23,10,20,28,22,-2,-1,25,-22,9,-22,3,-8,-5,10,18,-7,2,4,-1,-4,-17,29,29,29,-27,-16,-18,-14,-3,-12,19,-9,-1,-2,-14,16,-15,7,-4,24,-5,-14,-29,-21,-21,12,17,20,-10,-3,-16,19,7,-28,-22,-30,-28,-3,-23,11,8,14,11,19,24,-12,-25,10,2,-13,9,10,-12,-8,20,-14,14,8,24,-28,0,1,14,-28,2,-6,4,-19,-19,-28,21,-3,15,-28,25,-27,8,25,-29,-17,9,-21,-20,-21,6,-22,-6,-30,-13,-27,25,21,26,6,-19,-1,29,-30,-23,29,12,-5,-8,-25,19,18,-1,25,-9,3,15,0,-2,28,-19,-24,-17,26,-12,17,23,7,21,-25,2,6,10,18,-4,21,-14,-8,-27,24,26,-2,20,-29,-14,13,16,21,-26,-9,-20,9,-5,-7,13,-26,2,-30,13,-12,12,-27,27,-9,-19,7,-9,-2,-5,-16,29,25,26,0,6,27,-22,-1,-22,-1,13,-10,15,-29,24,14,27,-28,-16,10,3,9,-22,-8,-22,-25,-7,-3,5,26,-28,14,15,28,4,4,20,-5,-13,20,-30,5,-25,-23,-11,-14,-14,14,21,3,-25,-21,19,-19,11,-28,9,-4,-30,-3,-18,-8,-15,-6,-10,-17,-23,-2,22,-1,-11,28,9,3,-20,-6,8,5,14,26,24,-22,-17,-24,-15,-10,19,13,-10,-8,21,-7,12,-19,25,16,4,-7,28,23,-30,-2,4,27,8,13,-23,3,24,-15,-20,10,2,11,7,21,-2,20,-30,19,11,5,5,-29,21,28,-18,19,-28,29,9,-18,-26,-12,12,-15,-6,-13,29,23,7,-23,-19,-30,-11,-11,-25,19,-26,-28,-28,25,-2,29,6,3,-19,-18,27,20,23,25,-27,27,-30,-25,28,13,-25,-30,1,-14,-9,-15,27,2,28,28,-20,8,1,-19,-8,-4,6,10,-11,27,-18,-9,27,7,-1,-12,-16,3,-28,-8,-22,20,-5,-16,16,17,20,-29,22,-3,-1,-5,-11,18,2,-12,8,4,15,-14,5,25,17,-18,-17,-12,-10,18,-7,8,-30,-22,-28,-10,-30,14,-5,-9,16,-24,-16,0,2,4,-14,9,-2,1,-6,-7,10,-20,-1,0,25,27,-24,3,-10,27,-8,12,8,6,16,-14,-24,4,5,12,-7,-9,8,3,9,10,-8,24,12,-13,8,10,-23,4,10,16,20,7,8,-29,-11,-29,21,23,20,23,12,-26,-14,10,-2,21,-29,5,18,10,-27,-11,-22,-25,1,14,-12,1,-26,-11,-13,-2,7,10,-24,-15,-26,1,13,23,8,-26,29,8,-13,-11,-21,5,-25,13,-7,20,28,5,25,22,-23,7,-21,4,-8,9,-24,13,22,19,24,-27,2,23,28,-22,0,14,3,-27,-1,-17,27,12,-19,13,3,23,0,-26,28,-15,0,2,-11,4,-26,3,8,-15,-12,2,-12,-25,15,4,4,11,-18,9,6,5,26,-11,-22,6,17,-23,-14,-7,-24,-28,-25,-3,-15,18,10,-20,15,-17,-16,11,22,13,4,6,-10,-12,28,15,0,19,-30,-5,8,16,-23,4,-18,10,-1,-25,-8,-21,-13,5,-19,-8,-6,6,0,13,7,17,12,-3,-17,-21,16,-17,-3,13,10,-27,-1,-16,9,18,-1,5,-19,11,14,-12,-3,-1,-16,22,-9,19,-11,28,-14,-19,2,22,9,9,23,22,0,1,21,5,-3,10,-3,-8,-6,13,25,-19,26,9,-29,-26,13,-28,20,-2,20,12,6,3,22,-13,-29,-5,-22,-2,-14,-17,-2,7,24,27,17,-21,7,-21,9,19,26,-28,8,-20,-26,-9,22,-2,1,-9,-28,26,15,-13,-29,-25,-11,-23,2,15,6,-14,-18,-9,-4,-17,-30,-12,7,-19,-8,14,-29,-17,0,-5,-29,4,14,25,-29,4,-6,18,10,7,0,-19,21,29,2,21,17,-26,16,22,-24,18,19,-4,19,29,-6,0,23,-23,17,18,-30,4,23,17,17,14,-5,-9,-19,4,23,9,-14,23,18,19,4,20,17,24,13,11,-3,-16,29,9,11,23,26,-18,24,7,19,13,-20,14,11,-4,19,6,22,-2,8,-5,-15,29,14,23,-8,16,-21,29,5,15,16,3,15,-25,27,-23,-11,15,17,-29,-27,13,13,-11,6,18,9,-2,26,-11,-15,11,5,17,-3,25,11,6,-20,-19,8,-7,-9,-27,22,-21,-25,-28,-5,-17,-24,-28,26,-3,11,-28,21,-16,-18,4,-15,29,7,5,-26,22,-12,14,14,21,-25,29,-27,-4,-29,24,10,27,29,-5,21,-22,-4,-6,-28,1,-24,-4,25,11,-26,16,-13,-11,19,-15,17,-4,10,-11,16,-18,-8,-21,-8,-13,-9,5,-5,-7,-29,-7,22,-23,-26,12,13,17,-18,14,1,25,28,17,20,15,-12,11,5,-28,-28,3,11,17,23,-20,1,23,-4,23,13,-26,0,-12,22,18,-19,-1,-29,-12,-4,-8,9,-27,-11,-9,4,-11,2,-8,-17,-27,-10,0,18,-14,21,-11,-18,22,-18,-13,12,-22,28,27,-30,23,-22,-2,-17,-16,-2,-21,2,-4,9,23,-13,-25,-7,6,-22,7,-29,-21,28,1,-4,-12,-12,-25,-11,-8,19,-27,-5,-14,-15,-24,1,-30,29,3,24,8,-25,-8,7,5,4,-13,1,2,-30,-6,9,17,-13,-11,-26,11,-15,-5,-4,12,-28,-10,-6,-16,8,23,5,27,29,5,6,-23,8,16,16,0,-23,11,27,25,4,15,17,-19,-27,-17,-18,24,8,16,11,3,-27,-5,-29,-21,2,-22,-13,-17,19,-20,24,-28,-30,0,0,9,-16,12,-11,9,7,-7,10,-21,-28,-13,20,-7,22,-4,-24,14,12,-2,0,-10,-21,12,-1,13,10,-14,-17,3,-19,13,-10,3,-13,10,13,7,-8,-12,-30,12,-18,-11,24,-12,-6,-2,-19,-16,19,3,-12,-19,20,6,-28,27,28,12,-30,0,28,-30,-21,-17,-8,25,10,16,-10,-11,10,-24,4,13,-30,3,-28,23,-5,-18,-25,12,-1,16,12,-14,3,29,8,-30,21,5,-29,-21,-25,-28,-8,20,12,-22,-27,11,-11,14,22,2,7,-16,21,-2,-23,20,-28,3,29,-5,-20,-22,20,-16,-7,24,-16,20,18,0,-15,-29,-17,5,-21,7,-30,22,28,-29,28,21,10,-19,-7,27,4,1,-2,5,-26,-14,15,26,-13,20,-20,-23,-5,0,18,2,2,19,29,22,-20,-27,20,-14,-13,-5,-10,26,-10,-7,-22,-6,-12,29,9,-14,-1,-7,25,8,-25,12,-14,-1,22,24,-29,-16,-3,9,26,28,29,-10,24,-28,9,16,-29,-16,13,7,6,0,-12,-3,-27,-30,18,4,-13,-14,-12,20,1,12,-10,-6,-4,-22,11,-24,-26,22,-4,4,21,-17,27,5,5,5,14,-23,-7,24,-19,17,-6,0,17,15,-28,7,28,-30,-30,24,10,1,-3,1,20,5,12,26,12,-3,19,7,1,-24,-5,7,-2,10,-26,-26,7,16,4,2,27,-2,17,-9,13,-5,-15,-23,5,-8,15,24,-12,-5,2,-6,-23,-24,-25,29,22,-15,-16,-21,3,5,-7,10,-3,-13,-26,-10,24,9,9,-17,-5,5,-26,13,-15,5,-3,-5,10,3,23,3,-21,4,25,19,-25,-15,-15,-15,3,8,-5,25,-4,-23,10,29,24,1,24,6,-17,4,17,5,-14,-13,-1,-30,-5,21,-2,-28,10,-9,7,-25,15,12,3,0,16,22,19,2,-4,-21,-22,-2,-12,28,15,12,-27,27,-11,29,-10,22,26,-26,-30,16,0,7,-5,4,7,-19,-24,-3,-8,-10,0,-25,-26,-19,20,20,11,3,-18,23,-6,-2,-7,11,-20,-15,6,26,5,-14,-11,-8,17,-30,4,-13,-3,-4,-20,-4,13,-3,-22,23,11,27,17,17,-19,-30,-8,10,-5,3,-6,-28,-7,-15,-17,-17,-27,22,29,-6,14,6,23,-13,24,3,-21,-6,14,-7,19,14,-18,-17,7,-11,1,-24,-7,-10,0,11,13,-20,-17,4,-16,-7,1,15,-11,-18,-23,-13,3,-10,0,5,15,-25,7,4,13,-16,-12,21,-7,-7,-16,-4,-7,29,-3,26,-14,-14,-1,23,25,4,-3,27,3,7,15,21,-8,-17,-30,15,29,-6,-25,13,17,17,8,-10,-20,-23,-27,4,-8,0,25,-7,4,4,18,-26,22,0,10,0,8,-26,-1,-5,15,14,-23,7,12,-16,16,3,20,-27,-5,16,0,-28,-13,26,-10,24,20,-5,-12,14,26,0,19,9,-28,-26,3,10,3,-18,18,-29,-7,24,-26,16,-15,19,9,4,-12,-27,12,14,-6,-5,12,27,15,16,29,-27,-4,-21,12,15,21,-13,-19,12,-30,14,-9,2,-13,-14,8,7,9,-15,0,26,11,-23,-7,-16,26,7,-8,19,17,-4,-11,1,20,13,10,-10,-9,-19,-26,27,3,-5,-12,11,-5,18,-2,4,18,12,-19,7,-15,-10,7,26,-10,-10,-24,14,11,-12,-15,-19,-30,-29,12,-6,2,-16,-19,0,-16,16,-21,-14,23,-1,-5,-4,22,22,24,19,5,2,29,-13,19,3,-29,14,12,27,24,21,9,25,-26,-9,13,22,-5,-6,15,-17,3,27,-18,29,-8,-10,-22,-7,-14,-6,0,24,24,3,-22,-1,-15,21,0,25,4,-18,-9,10,-16,17,-16,21,12,-30,-22,6,-8,-18,-27,-27,28,-9,-2,-30,21,5,1,5,11,-25,9,-6,-17,17,8,-29,10,0,-25,19,-30,-3,-12,-4,27,-29,-1,22,23,-21,10,29,28,2,-6,12,-9,22,-12,-5,-17,-25,-11,28,3,-15,-21,20,13,-10,-12,1,28,25,-16,-5,-7,-22,15,26,-14,-10,-24,27,-24,-24,14,-11,7,-6,-10,8,4,-2,-26,-7,7,20,-7,-12,11,-7,0,1,19,-2,-15,19,-10,23,10,-4,3,7,0,23,-20,-7,-14,3,9,-6,-2,28,26,29,8,4,25,4,23,-24,17,0,-15,-6,29,25,-6,19,-15,-11,-20,-6,13,-9,17,7,-9,4,18,-25,25,-20,-3,5,0,3,7,-14,23,0,9,-26,-30,28,24,-10,0,-28,-21,-13,23,-28,-3,-19,-12,-20,-24,9,21,21,-26,29,12,21,-18,-19,7,1,-1,-21,4,-12,22,24,20,12,9,7,11,-16,-27,11,-16,-7,12,-19,-16,-29,28,24,-4,9,21,8,-16,-2,18,-9,-22,-2,24,-1,17,15,-18,26,-16,-27,24,-9,26,18,3,-12,-21,-20,-13,25,-3,16,-3,-7,18,-4,25,-22,-9,25,-21,-9,-18,-13,1,17,20,19,25,-22,9,-10,1,2,13,-12,1,-3,-3,16,28,15,0,-4,-12,-30,8,1,-24,5,28,24,-20,-2,3,-1,0,-22,14,27,8,2,-12,-28,12,-18,17,0,16,-14,-10,22,-19,1,-13,-7,-12,25,13,21,-13,-6,-5,-19,18,-13,-28,-1,-13,22,20,7,-9,-15,-11,-17,-27,5,21,28,20,12,25,25,4,-12,28,17,-14,-2,-6,-25,15,29,8,-10,-5,6,-9,-29,-29,25,9,-17,1,-4,-29,18,23,4,-20,14,4,18,-13,6,-13,19,-6,10,21,-17,-5,-16,26,-27,3,21,-21,28,25,-26,-28,23,-11,15,10,-27,19,-27,-12,-17,0,-24,8,8,-24,0,12,4,-27,-3,-7,-26,15,-29,-27,-25,25,20,5,-29,-23,0,27,23,0,-1,-2,6,-7,13,6,10,28,24,8,-14,-9,-8,24,-3,-11,-1,27,6,-29,17,0,19,9,-11,-7,-26,-27,10,26,-6,-10,-1,-14,19,28,22,19,8,20,-3,5,13,21,-7,-21,-25,2,-26,-17,28,7,25,-1,9,-14,-6,-24,26,-30,4,26,-4,20,-21,-22,6,17,-17,21,-25,-23,18,-13,16,29,8,-27,-26,9,-16,15,-30,-2,-16,-7,29,-2,2,-3,5,-21,13,10,5,4,15,-19,9,-24,28,17,9,21,-19,-3,-1,17,24,5,-14,-23,-8,-19,-10,-7,25,4,-6,24,-12,-19,17,-11,26,8,-16,28,-29,27,15,20,22,15,11,26,9,-21,3,-6,-22,-23,14,2],-52,2))
print('elapse time: {} sec'.format(time.time() - stime))

