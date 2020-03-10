import time

class Solution:
    def findShortestSubArray(self, nums: 'List[int]') -> int:
        tmps = set()
        unique = [v for v in nums if v not in tmps and not tmps.add(v)]
        freq = {}
        for u in unique:
            freq[u] = nums.count(u)
        freq = sorted(freq.items(), key=lambda param:param[1], reverse=True)
        mval = freq[0][1]
        freq = [v for v in freq if v[1] == mval]
        n = len(nums)
        lengths = []
        for f in freq:
            val = f[0]
            l = nums.index(val)
            r = n - nums[::-1].index(val) - 1
            lengths.append(r-l+1)
        return min(lengths)
        

stime = time.time()
sol = Solution()
print(sol.findShortestSubArray([1, 2, 2, 3, 1]))
print('elapse time: {} sec'.format(time.time() - stime))
