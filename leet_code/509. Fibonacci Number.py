class Solution:
    def fib_es(self, N: int) -> int:
        def fibo(N):
            if 0 == N:
                return 0
            if 1 == N:
                return 1
            return fibo(N-2)+fibo(N-1)
        return fibo(N)

    def fib(self, N: int) -> int:
        dp = {}
        def fibo(N):
            if 0 == N:
                return 0
            if 1 == N:
                return 1
            if N in dp:
                return dp[N]
            dp[N] = fibo(N-2)+fibo(N-1) 
            return dp[N]
        return fibo(N)
