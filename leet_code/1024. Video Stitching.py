
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def videoStitching(self, clips: [[int]], T: int) -> int:
        
        clips.sort(key=lambda p: p[0], reverse=False)
        cnt = 0
        
        while True:
            new_clips = []
            pn = len(clips)

            s = clips[0][0] - 1
            e = 0
            cnt = 0

            for ns, ne in clips:
                if e >= T:
                    break
                
                if e < ns:
                    return -1
                
                if s <= ns <= ne <= e:
                    continue

                if ns <= s <= e <= ne:
                    s = ns
                    e = ne
                    continue
                
                s = ns
                e = ne
                cnt += 1
                new_clips += [ns, ne],

            if pn == len(new_clips):
                break


            clips = new_clips
        
        return cnt if e >= T else -1


    def videoStitching(self, clips: [[int]], T: int) -> int:
        clips.sort(key=lambda p: p[0], reverse=False)
        pre_s = clips[0][0] - 1
        pre_e = 0                   # range must start from 0
        cnt = 0

        for s, e in clips:
            if pre_e >= T:
                break

            if pre_e < s: # discontinuity
                break

            if pre_s < s <= pre_e:
                pre_s = pre_e
                cnt += 1

            pre_e = max(pre_e, e)

        return cnt if cnt and pre_e >= T else -1


    def videoStitching(self, clips: [[int]], T: int) -> int:
        clips.sort(key=lambda p: p[0], reverse=False)
        ps = clips[0][0] - 1
        pe = 0
        cnt = 0

        for s, e in clips:
            if pe >= T:
                break

            if pe < s:
                break

            if ps <= s <= e <= pe:
                continue

            if ps < s <= pe:
                ps = pe
                cnt += 1

            pe = max(pe, e)

        return cnt if cnt and pe >= T else -1



stime = time.time()
#print(3 == Solution().videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10))
print(3 == Solution().videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))
print('elapse time: {} sec'.format(time.time() - stime))