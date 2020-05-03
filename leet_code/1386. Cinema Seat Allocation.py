
import time
import copy
import collections


class Solution:
    # memory limite for n = 1000000000
    def maxNumberOfFamilies(self, n: int, reservedSeats: [[int]]) -> int:
        seats = collections.defaultdict(list)
        for r, c in reservedSeats:
            seats[r] += c,

        for r in range(1, n + 1):
            if 1 not in seats[r]:
                seats[r] += 1,
            if 10 not in seats[r]:
                seats[r] += 10,

        for r in seats:
            seats[r].sort()

        cnt = 0
        for r in range(1, n + 1):
            start = 1
            if not seats[r]:
                cnt += (10 - start)//4
                continue
            
            for c in seats[r]:
                if c - start >= 4:
                    if (start == 3 or start == 5):
                        start += 1

                    cnt += (c - start)//4
                start = c + 1

        return cnt

    def maxNumberOfFamilies(self, n: int, reservedSeats: [[int]]) -> int:
        seats = collections.defaultdict(int)

        reservedSeats.sort(key=lambda p: p[0])

        for r, c in reservedSeats:
            seats[r] |= 1<<(c - 1)

        for r in range(1, n + 1):
            seats[r] |= 1 + (1<<10)

        cnt = 0

        for r, line in seats.items():
            #       |       |
            # 10 9 8 7 6 5 4 3 2 1 
            # 1  0 0 0 0 0 0 0 0 1
            #            0 0 0 0
            #    0 0 0 0
            #        0 0 0 0     

            if 0 == (line & 0x1E):
                line |= 0x1E
                cnt += 1

            if 0 == (line & 0x1E0):
                line |= 0x1E0
                cnt += 1

            if 0 == (line & 0x78):
                line |= 0x78
                cnt += 1


        return cnt

    def maxNumberOfFamilies(self, n: int, reservedSeats: [[int]]) -> int:
        reservedSeats.sort(key=lambda p: p[0])
        cnt = i = 0
        cur = 1
        items = len(reservedSeats)

        while i < items:
            r, c = reservedSeats[i]

            if cur < r:
                cnt += (r - cur)*2
                cur = r

            line = 1 + (1<<10)
            line |= 1<<(c - 1)

            while i + 1 < items and r == reservedSeats[i + 1][0]:
                line |= 1<<(reservedSeats[i + 1][1] - 1)
                i += 1

            if 0 == (line & 0x1E):
                line |= 0x1E
                cnt += 1

            if 0 == (line & 0x1E0):
                line |= 0x1E0
                cnt += 1

            if 0 == (line & 0x78):
                line |= 0x78
                cnt += 1

            i += 1
            cur += 1

        if r < n:
            cnt += (n - r)*2

        return cnt



stime = time.time()
print(4 == Solution().maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
print(2 == Solution().maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
print(4 == Solution().maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))
print(2 == Solution().maxNumberOfFamilies(5, [[4,7],[4,1],[3,1],[5,9],[4,4],[3,7],[1,3],[5,5],[1,6],[1,8],[3,9],[2,9],[1,4],[1,9],[1,10]]))
print(5 == Solution().maxNumberOfFamilies(3, [[2,3]]))
print(3 == Solution().maxNumberOfFamilies(4, [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]))
print('elapse time: {} sec'.format(time.time() - stime))