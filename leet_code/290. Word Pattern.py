import time

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        adict = {}
        registered = []
        str = list(str.split())
        np = len(pattern)
        n = len(str)
        if np != n:
            return False
        for i in range(n):
            if pattern[i] not in adict:
                if str[i] in registered:    # for case: 'abba', 'dog dog dog dog'
                    return False
                adict[pattern[i]] = str[i]
                registered.append(str[i])
            else:
                if adict[pattern[i]] != str[i]:
                    return False
        return True


    def wordPattern(self, pattern: str, str: str) -> bool:
        uniq = {}
        str = str.split()
        
        for i, ch in enumerate(pattern):
            print('ch = ', ch, uniq)
            if ch not in uniq:
                uniq[ch] = str[i]
            else:
                if uniq[ch] != str[i]:
                    return False
        return True


stime = time.time()
sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog")) # True
print(sol.wordPattern("aba", "cat cat cat dog"))
print(sol.wordPattern("abba", "dog dog dog dog")) # False
print('elapse time: {} sec'.format(time.time() - stime))