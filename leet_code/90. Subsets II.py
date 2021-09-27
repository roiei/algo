

class Solution:
    def get_combs(self, nums, n, r, depth, start, t, res):
        if depth == r:
            res.append(t[:])
            return
        for i in range(start, n):
            t.append(nums[i])
            self.get_combs(nums, n, r, depth+1, i+1, t, res)
            t.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(n+1):
            self.get_combs(nums, n, i, 0, 0, [], res)
        out = []
        for r in res:
            r.sort()
            if r not in out:
                out.append(r)
        return out

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def dfs(start, sel, num, limit, res):
            if num == limit:
                res.add(tuple(sorted(sel)))
                return
            
            for i in range(start, n):
                dfs(i + 1, sel + [nums[i]], num + 1, limit, res)
        
        res = set()
        for i in range(n + 1):
            dfs(0, [], 0, i, res)
        
        return res

