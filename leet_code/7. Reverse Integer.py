
class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x > float('inf') or x < float('-inf'):
            return 0
        sign = 1
        if x < 0:
            sign = -1
        xstr = str(x)
        if -1 == sign:
            xstr = xstr[1:]
        xstr = xstr[::-1]
        skip_cnt = 0
        for ch in xstr:
            if ch != '0':
                break
            skip_cnt += 1

        res = xstr[skip_cnt:]

        if '' == res:
            return 0
        if -1 == sign:
            res = '-' + res
        return int(res)


x = 123
#x = -123
#x = 120
#x = 901000
x = 1534236469  # 0

sol = Solution()
print(sol.reverse(x))

