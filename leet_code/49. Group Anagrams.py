import time
from util_list import *


class Solution:
    def is_anagram(self, str1, str2) -> bool:
        str1 = list(str1)
        str2 = list(str2)
        n = len(str1)
        if n != len(str2):
            return False

        for ch in str1:
            if ch in str2:
                str2.pop(str2.index(ch))
                continue
            return False
        return True

    def is_anagram2(self, str1, str2) -> bool:
        str1 = list(str1).sort()
        str2 = list(str2).sort()
        return True if str1 == str2 else False

    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        if not strs:
            return []
        uniqs = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s not in uniqs:
                uniqs[s] = []
            uniqs[s].append(word)
        out = []
        for k, v in uniqs.items():
            out.append(v)
        return out


stime = time.time()
print(Solution().is_anagram('dad', 'day'))
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
#print(Solution().groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"])

print('elapse time: {} sec'.format(time.time() - stime))
