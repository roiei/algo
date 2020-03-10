
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        si = ti = 0
        mn = float('inf')
        rsx = rex = 0
        
        
        while si < n:
            ti = 0
            sx = None
            ex = None
            
            sj = si
            while sj < n:
                if s[sj] == t[ti]:
                    if sx == None:
                        sx = sj
                    ti += 1
                    
                if ti == len(t):
                    ex = sj
                    break
                sj += 1
            
            if ex == None:
                break
            
            if ex != None and mn > ex - sx + 1:
                mn = ex - sx + 1
                rsx = sx
                rex = ex
            
            si = sx + 1
            
        return s[rsx:rex + 1] if mn != float('inf') else ''


    def minWindow(self, s, t):
        req = collections.Counter(t)
        len_req = len(req)

        sx = ex = 0
        i = 0
        wnd = []
        wnd_idx = []
        wnd_freq = collections.defaultdict(int)
        filled = 0
        mn = float('inf')
        t = list(t)

        while i < len(s):
            ch = s[i]
            if ch not in t:
                i += 1
                continue

            wnd += ch,
            wnd_idx += i,
            

            wnd_freq[ch] += 1
            if wnd_freq[ch] == req[ch]:
                filled += 1

            if filled == len_req:
                if wnd_idx[-1] - wnd_idx[0] + 1 < mn:
                    mn = wnd_idx[-1] - wnd_idx[0] + 1
                    sx = wnd_idx[0]
                    ex = wnd_idx[-1]

                while wnd and wnd[0] != t[0]:
                    wnd_idx.pop(0)
                    ch = wnd.pop(0)
                    wnd_freq[ch] -= 1
                    if wnd_freq[ch] < req[ch]:
                        filled -= 1

            i += 1
        return s[sx:ex + 1] if mn != float('inf') else ''





stime = time.time()
print('bcde' == Solution().minWindow('abcdebdde', 'bde'))
print('' == Solution().minWindow('jmeqksfrsdcmsiwvaovztaqenprpvnbstl', 'u'))
print('kzxwqegknd' == Solution().minWindow('fgrqsqsnodwmxzkzxwqegkndaa', 'kzed'))
print('' == Solution().minWindow('hpsrhgogezyfrwfrejytjkzvgpjnqil', 'tgr'))
print('elapse time: {} sec'.format(time.time() - stime))