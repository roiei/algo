
class Solution(object):
    def countBits_es(self, num):
        res = []
        while num:
            res.insert(0, '{:b}'.format(num).count('1'))
            num -= 1
        res.insert(0, 0)
        return res

    def countBits(self, num):
        dp = [0]*(num+1)
        for i in range(1, num+1):
            if 0 == i%2:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2]+1
        return dp
            
        
