import time


class Solution:
    def longestWord(self, words: 'List[str]') -> str:
        candidates = []
        for word in words:
            check = []
            for i in range(1, len(word)):
                check.append(True if word[:i] in words else False)
            if all(check):
                candidates.append(word)
        candidates.sort()
        return max(candidates, key=len)


stime = time.time()
sol = Solution()
# print(sol.longestWord(["w","wo","wor","worl", "world"])) # "world"
# print(sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])) # "apple"
print(sol.longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"])) # yodn
print('elapse time: {} sec'.format(time.time() - stime))