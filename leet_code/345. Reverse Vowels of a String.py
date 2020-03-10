class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        string = list(s)
        for i in range(len(string)):
            if ('a' == s[i] or 'e' == s[i] or 'i' == s[i] 
                or 'o' == s[i] or 'u' == s[i] or
                'A' == s[i] or 'E' == s[i] or 'I' == s[i] 
                or 'O' == s[i] or 'U' == s[i]):
                vowels.append(s[i])
        vowels.reverse()
        for i in range(len(string)):
            if ('a' == s[i] or 'e' == s[i] or 'i' == s[i] 
                or 'o' == s[i] or 'u' == s[i] or
                'A' == s[i] or 'E' == s[i] or 'I' == s[i] 
                or 'O' == s[i] or 'U' == s[i]):
                string[i] = vowels.pop(0)

        return ''.join(string)


s = 'hello'
s = 'aA'

stime = time.time()
sol = Solution()
ret = sol.reverseVowels(s)
print('1: {} sec'.format(time.time() - stime))
print(ret)