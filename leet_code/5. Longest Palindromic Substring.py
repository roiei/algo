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

    def longestPalindrome_(self, s: str) -> str:
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


    def longestPalindrome(self, s: str) -> str:
        if '' == s:
            return ''

        n = len(s)
        l = 0
        r = n-1
        
        rs = s[::-1]
        toggle = True
        q = [(l, r)]
        mem = {}
        
        while q:
            l, r = q.pop(0)
            if (l, r) in mem:
                continue
            if rs[n-r-1:n-l] == s[l:r+1]:
                return s[l:r+1]

            if l <= r:
                q += (l+1, r),
                q += (l, r-1),
            
            mem[(l, r)] = True

        return ''

    def longestPalindrome(self, s: str) -> str:
        i = 0;
        n = len(s)
        palin = ''
        plen = 0

        while i < n:
            l = i
            r = i

            if r < n - 1 and s[r] == s[r+1]:
                r += 1

            while l > 0 and r < n-1 and s[l] == s[r]:
                l -= 1
                r += 1

            length = len(s[l:r+1])
            if length > plen:
                palin = s[l:r+1]
                plen = length

            # while l >= 0 and r < n and s[l] == s[r]:
            #     l -= 1
            #     r += 1

            # length = len(s[l+1:r])
            # if length > plen:
            #     palin = s[l+1:r]
            #     plen = length

            i += 1
        return palin

    def longestPalindrome(self, s: str) -> str:
        i = 0;
        n = len(s)
        palin = ''
        plen = 0

        while i < n:
            l = i
            r = i

            while r + 1 < n and s[r] == s[r + 1]:
                r += 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            length = len(s[l+1:r])
            if length > plen:
                palin = s[l+1:r]
                plen = length

            i += 1
        return palin

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = 0
        res = ''

        for i in range(n):
            l = r = i
            while r + 1 < n and s[i] == s[r + 1]:
                r += 1

            while l - 1 >= 0 and  r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            length = len(s[l:r + 1])
            if mx < length:
                mx = length
                res = s[l:r + 1]

        return res



#print(Solution().longestPalindrome("ccd"))
#print(Solution().longestPalindrome("abb"))
print('bccb' == Solution().longestPalindrome("eabccb"))
print('aba' == Solution().longestPalindrome_stack("babad"))
print('kjxjk' == Solution().longestPalindrome_stack("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni"))

# ret = sol.longestPalindrome("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu")
# print(ret)
