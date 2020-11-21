
import time
import copy
import collections


class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        n = len(coordinates)
        m = pm = None

        for i in range(n - 1):
            xdiff = coordinates[i][0] - coordinates[i + 1][0]
            ydiff = coordinates[i][1] - coordinates[i + 1][1]
            if xdiff != 0:
                m = ydiff/xdiff
            else:
                m = 1

            if pm != None:
                if pm != m:
                    return False

            pm = m

        return True


stime = time.time()
print(True == Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(False == Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(True == Solution().checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))
print('elapse time: {} sec'.format(time.time() - stime))