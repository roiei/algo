
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ''
        
        required = collections.Counter(t)
        len_required = len(required)
        
        l, r = 0, 0
        kind = 0
        mn = float('inf')
        si = ei = 0
        
        wnd = collections.defaultdict(int)
        
        while r < len(s):
            ch = s[r]
            if ch not in t:
                r += 1
                continue
            
            wnd[ch] += 1
            
            if wnd[ch] == required[ch]:
                kind += 1
            
            while l <= r and kind == len_required:
                ch = s[l]
                if ch not in t:
                    l += 1
                    continue
                
                if mn > r - l + 1:
                    mn = r - l + 1
                    si = l
                    ei = r
                
                wnd[ch] -= 1
                if wnd[ch] < required[ch]:
                    kind -= 1
                
                l += 1
            
            r += 1
        
        if mn == float('inf'):
            return ''
        return s[si:ei + 1]

    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        req = collections.Counter(t)
        wnd = collections.defaultdict(int)
        num_kind = 0
        mn = float('inf')
        ml = mr = 0
        
        while r < len(s):
            ch = s[r]
            if ch not in t:
                r += 1
                continue
            
            wnd[ch] += 1

            if wnd[ch] == req[ch]:
                num_kind += 1
            
            while l <= r and num_kind == len(req):
                ch = s[l]
                if ch not in t:
                    l += 1
                    continue
                
                if mn > r - l + 1:
                    mn = r - l + 1
                    mr = r
                    ml = l
                
                wnd[ch] -= 1
                if wnd[ch] < req[ch]:
                    num_kind -= 1
                
                l += 1
            
            r += 1
        
        return s[ml:mr + 1] if mn != float('inf') else ''


stime = time.time()
print('BANC' == Solution().minWindow('ADOBECODEBANC', 'ABC'))
print('ABA' == Solution().minWindow('ADCABCDEAKABAE', 'AAB'))
print('' == Solution().minWindow("a", "aa"))
print("ab" == Solution().minWindow("bdab", "ab"))
print('elapse time: {} sec'.format(time.time() - stime))
