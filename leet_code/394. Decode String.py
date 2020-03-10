
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, l, r):
            res = ''
            while l < r:
                if s[l] == ']':
                    break

                if 'a' <= s[l] <= 'z' or 'A' <= s[l] <= 'Z':
                    res += s[l]
                    l += 1
                    continue
                
                num = 0
                while l < r and ('0' <= s[l] <= '9'):
                    num = num*10 + int(s[l])
                    l += 1
                
                l += 1      # for '['
                ret, l = dfs(s, l, r)
                res += ret*num
            
            return res, l+1
        
        dstr, l = dfs(s, 0, len(s))
        return dstr


sequence = "3[a]2[bc]"
sequence = '3[a2[c]]'
sequence = "2[abc]3[cd]ef"
sequence = "3[a]2[b4[F]c]"

sol = Solution()
ret = sol.decodeString(sequence)
print(ret)
