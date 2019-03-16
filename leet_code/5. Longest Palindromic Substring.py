class Solution:
    cache = {}

    def lps(self, s):
        if len(s) == 1:
            return True, s

        if s in self.cache:
            return True, self.cache[s]

        if s == s[::-1]:
            return True, s

        is_palin_l, palin_l = self.lps(s[1:])
        is_palin_r, palin_r = self.lps(s[:-1])

        palin_l_len = palin_r_len = 0
        if True == is_palin_l:
            palin_l_len = len(palin_l)
        if True == is_palin_r:
            palin_r_len = len(palin_r)

        palin = palin_r if palin_l_len < palin_r_len else palin_l

        if True == is_palin_l or True == is_palin_r:
            self.cache[s] = palin

        return True if True == is_palin_l or True == is_palin_r else False, palin

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        self.cache.clear()
        is_palin, palin = self.lps(s)
        return palin

    def longestPalindrome_stack(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s

        res = []
        res_len = []
        stk = []
        stk.append(s[1:])
        stk.append(s[:-1])
        self.cache.clear()

        while True:
            nstk = []
            idx = 0
            while stk:
                s = stk.pop()
                if s in self.cache:
                    continue
                if len(s) <= 1:
                    res.append(s)
                    res_len.append(len(s))
                    continue
                if s == s[::-1]:
                    res.append(s)
                    res_len.append(len(s))
                    continue
                nstk.append(s[1:])
                nstk.append(s[:-1])
                idx += 1
                self.cache[s] = s[:]
            stk = nstk
            if not stk:
                break

        if res_len:
            return res[res_len.index(max(res_len))]
        return ''


sol = Solution()
ret = sol.longestPalindrome_stack("babad")
print(ret)


ret = sol.longestPalindrome_stack("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni")
print(ret)

ret = sol.longestPalindrome("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu")
print(ret)
