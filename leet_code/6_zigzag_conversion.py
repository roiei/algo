
class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if s == "":
            return ""
        if numRows == 1:
            return s
        # 1. split
        splits = [[] for i in range(numRows)]
        for i in range(0, len(s), numRows+(numRows-2)):
            for j in range(numRows):
                if i+j < len(s):
                    print('1. s[{} + {}] = {}'.format(i, j, s[i+j]))
                    splits[j].append(s[i+j])
            idx = 1
            for j in range(numRows-2, 0, -1):
                if i+numRows+j-1 < len(s):
                    #print('2. s[{} + {} + {}] = {}'.format(i, numRows, j, s[i+numRows+j-1]))
                    splits[idx].append(s[i+numRows+j-1])
                    idx += 1

        ret = ''
        for s in splits:
            sstr = ''
            for ch in s:
                sstr += ch
            ret = ret + sstr
        return ret


# P   A   H   N
# A P L S I I G
# Y   I   R

# PAY P ALI S HIR I NG

# s = "PAYPALISHIRING"
# numRows = 3
# expected_output = "PAHNAPLSIIGYIR"


s = "PAYPALISHIRING"
numRows = 4
#expected_output = "PINALSIGYAHRPI"

s = "A"
numRows = 1
expected_output = ''

s = "ABCDE"
numRows = 4
expected_output = "ABCED"


sol = Solution()
print(sol.convert(s, numRows))
print(expected_output)

