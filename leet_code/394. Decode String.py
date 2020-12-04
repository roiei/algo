
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

    def decodeString(self, s: str) -> str:
        n = len(s)

        def dfs(i):
            substr = ''
            num = ''

            while i < n:
                while i < n and s[i].isalpha():
                    substr += s[i]
                    i += 1

                while i < n and s[i].isdigit():
                    num += s[i]
                    i += 1

                if i < n and s[i] == '[':
                    i, res = dfs(i + 1)
                    num = int(num) if num else 1
                    substr += num*res
                    num = ''
                elif i < n and s[i] == ']':
                    break

            return i + 1, substr

        i, res = dfs(0)
        return res


# [a] : just return the letter(s)
# [a2[c]] : 
#       [c] : just return the letter(s)
#       multiply 2 
#       a + ...


print("aaabcbc" == Solution().decodeString("3[a]2[bc]"))
print("accaccacc" == Solution().decodeString("3[a2[c]]"))
print("abcabccdcdcdef" == Solution().decodeString("2[abc]3[cd]ef"))
print("abccdcdcdxyz" == Solution().decodeString("abc3[cd]xyz"))
