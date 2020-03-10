class Solution:
    def get_comb(self, nums, n, r, depth, trace, start, combs):
        if depth == r:
            combs.append(trace[:])
            return
        for i in range(start, n):
            for j in range(len(nums[i])):
                trace.append(nums[i][j])
                self.get_comb(nums, n, r, depth+1, trace, i+1, combs)
                trace.pop()

    def smallestRange(self, nums: 'List[List[int]]') -> 'List[int]':
        if not nums:
            return []
        combs = []
        n = len(nums)
        self.get_comb(nums, n, n, 0, [], 0, combs)
        diffs = []
        for comb in combs:
            comb.sort()
            diff = abs(comb[0]-comb[n-1])
            diffs.append([diff, [comb[0], comb[n-1]]])

        if diffs:
            diffs.sort(key=lambda param:param[0])
            return diffs[0][1]
        return []


lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
lists = [[10,10],[11,11]]
lists = [[1,2,3],
         [1,2,3],
         [1,2,3]]

lists = [[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]

stime = time.time()
sol = Solution()
ret = sol.smallestRange(lists)
print('elapse time: {} sec'.format(time.time() - stime))
print(ret)