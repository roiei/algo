
class Solution(object):

    def wordBreak(self, s, words):
        '''
        this algorithm meets timeout @ 91% of LintCode
        '''
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
    
        return ok[-1]


    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0
        
        n = len(s)
        dp = [False]*(n + 1)
        dp[0] = True
        
        longest_len = max([len(w) for w in dict])
        
        for i in range(1, n + 1):
            for j in range(max(0, i - longest_len), i):
                if not dp[j]:
                    continue
                
                if s[j:i] in dict:
                    dp[i] = True
                    break

        return dp[-1]