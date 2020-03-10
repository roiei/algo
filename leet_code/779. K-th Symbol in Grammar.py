class Solution:
    def get_val(self, depth, N, K, val):
        if depth == N:
            return val
        half = 2**((N-depth)-1)
        if K <= half:
            return self.get_val(depth+1, N, K, 0 if val == 0 else 1)
        else:
            return self.get_val(depth+1, N, K-half, 1 if val == 0 else 0)

    def kthGrammar(self, N: int, K: int) -> int:
        return self.get_val(1, N, K, 0)


stime = time.time()
sol = Solution()
print(sol.kthGrammar(1, 1)) # 0
print(sol.kthGrammar(2, 1)) # 0 
print(sol.kthGrammar(2, 2)) # 1
print(sol.kthGrammar(4, 5)) # 1
print(sol.kthGrammar(3, 4)) # 0
print(sol.kthGrammar(30, 434991989)) # 0
print('elapse time: {} sec'.format(time.time() - stime))