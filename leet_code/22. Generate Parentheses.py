

class Solution:
    def generateParenthesis(self, n):
        def generate(s, open_cnt, close_cnt, n, res):
            if open_cnt < n:
                generate(s+'(', open_cnt+1, close_cnt, n, res)
            if open_cnt > close_cnt:
                generate(s+')', open_cnt, close_cnt+1, n, res)
            if n == close_cnt:
                res.append(s)
        res = []
        generate('', 0, 0, n, res)
        return res

print(Solution().generateParenthesis(4))
