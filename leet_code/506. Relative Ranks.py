import time


class Solution:
    def findRelativeRanks(self, nums):
        n = len(nums)
        score_widx = [[nums[i], i] for i in range(len(nums))]
        score_widx.sort(key=lambda param:param[0], reverse=True)
        rank = []
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ml = min(n, len(medals))
        for i in range(ml):
            rank.append([medals[i], score_widx[i][1]])
        ll = n - i
        cur_rank = 4
        for j in range(i+1, i+ll):
            rank.append([str(cur_rank), score_widx[j][1]])
            cur_rank+= 1
        rank.sort(key=lambda param:param[1])
        only_rank = [val[0] for val in rank]
        return only_rank



stime = time.time()
sol = Solution()
print(sol.findRelativeRanks([5, 4, 3, 2, 1])) # 
print(sol.findRelativeRanks([10,3,8,9,4]))
print('elapse time: {} sec'.format(time.time() - stime)) 