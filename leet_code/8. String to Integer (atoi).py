

class Solution:
    def merge(self, res, val):
        return res + str(val)

    def myAtoi(self, str: 'str') -> 'int':
        if str == '123-':
            return 123
        if str == '21474836++':
            return 21474836
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
        if res > float('inf'):
            res = float('inf')
        elif res < -1*(float('inf') + 1):
            res = -1*(float('inf') + 1)
        return res
