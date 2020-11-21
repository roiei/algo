

class SolutionRmDup:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        
        while True:
            same = 1
            same_pos = []
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    same += 1
                else:
                    same = 1

                if same == k:
                    same_pos += i,
                    break

            if not same_pos:
                break

            for pos in same_pos:
                if pos < len(s):
                    s[pos - k + 1:pos + 1] = []
        
        return ''.join(s)


print('aa' == SolutionRmDup().removeDuplicates("deeedbbcccbdaa", 3))
print('ps' == SolutionRmDup().removeDuplicates("pbbcggttciiippooaais", 2))