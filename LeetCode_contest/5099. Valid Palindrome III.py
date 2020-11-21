


class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        
        def recur(l, r, k):
            if l < r and k == 0:
                return False
            if (l, r) in mem and mem[(l, r)]:
                return mem[(l, r)]

            if l >= r:
                return True

            ret = False
            if s[l] == s[r]:
                ret |= recur(l + 1, r - 1, k)
            elif k > 0:
                ret |= recur(l + 1, r, k - 1)
                if ret:
                    mem[(l, r)] = True
                    return True
                ret |= recur(l, r - 1, k - 1)
            mem[(l, r)] = ret
            return ret
        
        mem = {}
        return recur(0, n - 1, k)


    

    def isValidPalindrome(self, s, k):
            
        m = n = len(s)
        rs = s[::-1]

        dp = [[0]*(n + 1) for _ in range(m + 1)] 
          
        for i in range(m + 1): 
            for j in range(n + 1): 
                  
                # If first string is empty, 
                # only option is to remove 
                # all characters of second string 
                if not i: 
                    dp[i][j] = j    # Min. operations = j 
      
                # If second string is empty, 
                # only option is to remove 
                # all characters of first string 
                elif not j: 
                    dp[i][j] = i    # Min. operations = i 
      
                # If last characters are same, 
                # ignore last character and 
                # recur for remaining string 
                elif (s[i - 1] == rs[j - 1]): 
                    dp[i][j] = dp[i - 1][j - 1] 
      
                # If last character are different,  
                # remove it and find minimum 
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j],  # Remove from str1 
                                      (dp[i][j - 1])) # Remove from str2 

        return dp[m][n] <= k*2


    def isValidPalindrome(self, s, k):
        m = n = len(s)
        rs = s[::-1]

        dp = [[0]*(n + 1) for _ in range(m + 1)]
          
        for i in range(m + 1):
            for j in range(n + 1): 
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s[i - 1] == rs[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] 
                else: 
                    dp[i][j] = min(dp[i - 1][j], (dp[i][j - 1])) + 1

        return dp[m][n] <= k*2
      


print(True == Solution().isValidPalindrome("fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd",
216))
#print(True == Solution().isValidPalindrome('abcdeca', 2)) # removing b anc e