

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        keys = collections.defaultdict(list)
        keys['2'] = ['a', 'b', 'c']
        keys['3'] = ['d', 'e', 'f']
        keys['4'] = ['g', 'h', 'i']
        keys['5'] = ['j', 'k', 'l']
        keys['6'] = ['m', 'n', 'o']
        keys['7'] = ['p', 'q', 'r', 's']
        keys['8'] = ['t', 'u', 'v']
        keys['9'] = ['w', 'x', 'y', 'z']
        
        def dfs(digits, k, start, trace, res):
            if k == 0:
                res += ''.join(trace),
                return
            
            for i in range(len(keys[digits[start]])):
                dfs(digits, k - 1, start + 1, trace + [keys[digits[start]][i]], res)
        
        res = []
        dfs(digits, len(digits), 0, [], res)
        return res

sol = Solution()
ret = sol.letterCombinations('23')
print(ret)
        

