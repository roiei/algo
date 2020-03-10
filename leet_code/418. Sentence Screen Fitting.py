
class Solution:
    def check(self, rows, cols, sentence):
        nums = len(sentence)
        fitted = 0
        cur = 0

        for y in range(rows):
            line = ''
            x = 0
            while x < cols:
                left_line = cols - x
                if left_line >= len(sentence[cur]):
                    line += sentence[cur]
                    x += len(sentence[cur])
                    cur += 1
                    if cur == nums:
                        fitted += 1
                        cur = 0
                    left_line = cols - x
                    if left_line >= 1:
                        line += '-'
                        x += 1
                else:
                    break
            for i in range(cols - len(line)):
                line += '-'
        return fitted

    def check2(self, rows, cols, sentence):
        n = len(sentence)
        cur = 0
        cnt = 0
        for y in range(rows):
            x = 0
            line = ''

            while True:
                if len(line) + len(sentence[cur]) <= cols:
                    line += sentence[cur]

                    if cur + 1 == n:
                        cur = 0
                        cnt += 1
                        print('. = ', line)
                        line = ''
                    else:
                        cur += 1
                else:
                    break

                if len(line) + 1 <= cols:
                    line += '-'
                else:
                    break

        return cnt


print(Solution().check(2, 8, ["hello", "world"]))
print(Solution().check2(2, 8, ["hello", "world"]))
print()
print(Solution().check(3, 6, ["a", "bcd", "e"]))
print(Solution().check2(3, 6, ["a", "bcd", "e"]))
print()
print(Solution().check(4, 5, ["I", "had", "apple", "pie"]))
print(Solution().check2(4, 5, ["I", "had", "apple", "pie"]))


