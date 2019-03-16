
class Solution:
    def decode(self, s, i):
        res = ''
        while i < len(s) and s[i] != ']':
            if not ('0' <= s[i] <= '9'):
                res+= s[i]
                i+= 1
            else:
                n = 0
                while i < len(s) and '0' <= s[i] <= '9':
                    n = n*10 + int(s[i])
                    i+= 1

                i+= 1
                t, i = self.decode(s, i)
                i+= 1

                while n > 0:
                    res+= t
                    n-= 1

        return res, i

    def decodeString(self, s):
        dec_str, len = self.decode(s, 0)
        return dec_str;


sequence = "3[a]2[bc]"
sequence = '3[a2[c]]'
sequence = "2[abc]3[cd]ef"
sequence = "3[a]2[b4[F]c]"

sol = Solution()
ret = sol.decodeString(sequence)
print(ret)
