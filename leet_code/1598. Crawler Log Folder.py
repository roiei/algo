

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for log in logs:
            if log == '../':
                if stk:
                    stk.pop()
                continue
            elif log == './':
                continue

            stk += log,

        return len(stk)
