
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
                #print('left = ', left_line)
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
            print('line = ', line)
        print('fitted = ', fitted)



rows = 2
cols = 8
sentence = ["hello", "world"]

rows = 3
cols = 6
sentence = ["a", "bcd", "e"]

rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]

sol = Solution()
ret = sol.check(rows, cols, sentence)
print(ret)
