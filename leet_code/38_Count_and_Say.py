class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1'

        for i in range(1, n):
            next = ''
            j = 0

            while j < len(cur):
                same_cnt = 1     # at least 1

                while j < len(cur) - 1:
                    if cur[j] != cur[j + 1]:
                        break
                    same_cnt += 1
                    j += 1

                next += str(same_cnt)
                next += cur[j]
                j += 1

            cur = next

        return cur

    def countAndSay(self, n: int) -> str:
        cur = '1'

        for i in range(1, n):
            next = ''
            j = 0

            while j < len(cur):
                cnt = 1

                while j < len(cur) - 1:
                    if cur[j] != cur[j +1]:
                        break
                    cnt += 1
                    j += 1

                next += str(cnt) + cur[j]
                j += 1

            cur = next

        return cur





sol = Solution()
print(sol.countAndSay(1))