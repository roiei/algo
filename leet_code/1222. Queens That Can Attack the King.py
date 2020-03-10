
import time
import copy
import collections


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        ky, kx = king
        
        dirs = collections.defaultdict(list)
        
        for qy, qx in queens:
            if qy == ky and qx != kx:
                if kx < qx: # R
                    if not dirs['R']:
                        dirs['R'] = (qy, qx)
                    elif dirs['R'] and dirs['R'][1] > qx:
                        dirs['R'] = (qy, qx)
                else:   # L
                    if not dirs['L']:
                        dirs['L'] = (qy, qx)
                    elif dirs['L'] and dirs['L'][1] < qx:
                        dirs['L'] = (qy, qx)    
            elif qx == kx and qy != ky:
                if ky < qy: # D
                    if not dirs['D']:
                        dirs['D'] = (qy, qx)
                    elif dirs['D'] and dirs['D'][0] > qy:
                        dirs['D'] = (qy, qx)
                else:   # U
                    if not dirs['U']:
                        dirs['U'] = (qy, qx)
                    elif dirs['U'] and dirs['U'][0] < qy:
                        dirs['U'] = (qy, qx)
            elif abs(kx - qx) == abs(ky - qy):
                if kx > qx and ky > qy: # UL
                    if not dirs['UL']:
                        dirs['UL'] = (qy, qx)
                    elif dirs['UL'] and dirs['UL'][1] < qx and dirs['UL'][0] < qy:
                        dirs['UL'] = (qy, qx)
                elif kx > qx and ky < qy:   # DL
                    if not dirs['DL']:
                        dirs['DL'] = (qy, qx)
                    elif dirs['DL'] and dirs['DL'][1] < qx and dirs['DL'][0] > qy:
                        dirs['DL'] = (qy, qx)
                elif kx < qx and ky > qy:   # UR
                    if not dirs['UR']:
                        dirs['UR'] = (qy, qx)
                    elif dirs['UR'] and dirs['UR'][1] > qx and dirs['UR'][0] < qy:
                        dirs['UR'] = (qy, qx)
                elif kx < qx and ky < qy:   # DR
                    if not dirs['DR']:
                        dirs['DR'] = (qy, qx)
                    elif dirs['DR'] and dirs['DR'][1] > qx and dirs['DR'][0] > qy:
                        dirs['DR'] = (qy, qx)
            
        res = []
        for dir in ['R', 'L', 'D', 'U', 'UL', 'DL', 'UR', 'DR']:
            if dirs[dir]:
                res += list(dirs[dir]),
        
        return res
                

stime = time.time()
#print([[0,1],[1,0],[3,3]] == Solution().queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
print([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]] == Solution().queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]))
#print([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]] == Solution().queensAttacktheKing([[4, 5], [5, 6]], [3,4]))
print('elapse time: {} sec'.format(time.time() - stime))