class Solution:
    def licenseKeyFormatting(self, S, K):
        out = ''
        idx = S.find('-')
        if -1 != idx:
            out += S[:idx]
        S = S[idx:]
        S = S.replace('-', '')

        out += '-'
        idx = 0
        chunk_len = K
        while idx < len(S):
            if chunk_len > 0:
                out += S[idx]
                chunk_len -= 1
                idx += 1
            else:
                out += '-'
                chunk_len = K

        out = out.upper()
        return out

        

s = "5F3Z-2e-9-w"    #output = "5F3Z-2E9W"
K = 4 

# s = "2-5g-3-J"       #output = "2-5G-3J"
# K = 2

s = "2-4A0r7-4k"        # "24A0-R74K"
K = 4

sol = Solution()
ret = sol.licenseKeyFormatting(s, K)
print(ret)