

class Solution:
    def merge(self, res, val):
        return res + str(val)

    def myAtoi(self, str: 'str') -> 'int':
        num = []
        sign_idx = -1
        sign = 1
        idx_1st_num = -1
        str = str.strip()
        for idx in range(len(str)):
            if '0' <= str[idx] <= '9':
                idx_1st_num = idx
                break
        for idx in range(len(str)):
            if str[idx] == '-' or str[idx] == '+':
                sign = -1 if str[idx] == '-' else 1
                sign_idx = idx
                break
        if -1 != idx_1st_num and -1 != sign_idx:
            if idx_1st_num < sign_idx:
                return 0
        #print('sign_idx = ', sign_idx)
        if -1 != sign_idx:
            str = str[sign_idx+1:]
        for ch in str:
            if '0' <= ch <= '9':
                num.append(int(ch))
            else:
                break
        if not num:
            return 0
        res = ''
        for n in num:
            res = self.merge(res, n)
        res = int(res)*sign
        if res > 0x7FFFFFFF:
            res = 0x7FFFFFFF
        elif res < -1*(0x7FFFFFFF + 1):
            res = -1*(0x7FFFFFFF + 1)
        return res


s = Solution()
print(s.myAtoi('+1'))
print(s.myAtoi('454654565456'))
print(s.myAtoi("  0000000000012345678"))
print(s.myAtoi("-   42"))
print(s.myAtoi("0-1"))

