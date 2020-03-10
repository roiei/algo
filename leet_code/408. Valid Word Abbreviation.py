
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        m = len(word)
        n = len(abbr)
        i = j = 0
        
        while i < m and j < n:
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
                continue
        
            digit = ''
            while j < n and abbr[j].isdigit():
                digit += abbr[j]
                j += 1

            if int(digit) > 0 and digit[0] == '0':
                return False
            
            digit = int(digit)
            
            if i + digit > m:
                return False
            
            i += digit
        
        return True



stime = time.time()
print(True == Solution().validWordAbbreviation('internationalization', 'i12iz4n'))
print(False == Solution().validWordAbbreviation('apple', 'a2e'))
print(True == Solution().validWordAbbreviation('a', '1'))
print(False == Solution().validWordAbbreviation('a', '01'))
print('elapse time: {} sec'.format(time.time() - stime))