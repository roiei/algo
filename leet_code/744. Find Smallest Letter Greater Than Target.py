import time

class Solution:
    def nextGreatestLetter(self, letters: 'List[str]', target: str) -> str:
        if not letters:
            return
        letters.sort()
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]


stime = time.time()
sol = Solution()
#print(sol.nextGreatestLetter(["c", "f", "j"], 'a')) # c
# print(sol.nextGreatestLetter(["c", "f", "j"], 'c')) # f
# print(sol.nextGreatestLetter(["c", "f", "j"], 'd')) # f
# print(sol.nextGreatestLetter(["c", "f", "j"], 'g')) # j
# print(sol.nextGreatestLetter(["c", "f", "j"], 'j')) # c
print(sol.nextGreatestLetter(["c", "f", "j"], 'k')) # c
print('elapse time: {} sec'.format(time.time() - stime))