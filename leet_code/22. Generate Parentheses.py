

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

    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opn, close, seq, res):
            if opn == n and close == n:
                res += seq,
                return

            if opn < n:
                dfs(opn + 1, close, seq + '(', res)
            
            if close < opn:
                dfs(opn, close + 1, seq + ')', res)
        
        res = []
        dfs(0, 0, '', res)
        return res
        

print(Solution().generateParenthesis(4))
