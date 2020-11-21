class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        time = time.split(':')
        nums = []
        for t in time:
            for ch in t:
                nums += int(ch),
        
        anchor = nums[0]*10*60 + nums[1]*60 + nums[2]*10 + nums[3]
        
        def dfs(nums, n, k, trace, res):
            if k == 0:
                hour = int(''.join([str(trace[0]), str(trace[1])]))
                minute = int(''.join([str(trace[2]), str(trace[3])]))

                if 0 <= hour <= 24:
                    if not (hour == 24 and minute > 0):
                        if minute < 60:
                            res += trace,
                return
        
            for i in range(n):
                dfs(nums, n, k - 1, trace + [nums[i]], res)
            
        res = []
        dfs(nums, len(nums), len(nums), [], res)

        time = []
        for r in res:
            time += r[0]*10*60 + r[1]*60 + r[2]*10 + r[3],

        time.sort()

        time += 24*60 + time[0],
        
        for t in time:
            if t > anchor:
                if t >= 24*60:
                    t -= 24*60
                res = '{:02}:{:02}'.format(t//60, t%60)
                return res
        return ''


#print('17:33' == Solution().nextClosestTime("17:31"))
#print("22:22" == Solution().nextClosestTime("23:59"))
print("00:00" == Solution().nextClosestTime("09:59"))
