import time
import heapq


class Solution:
    def getSkyline_es(self, buildings):
        if not buildings:
            return []

        temp = sorted(buildings, key=lambda p: p[1], reverse=True)
        width = temp[0][1]+1
        outline = [[i, 0] for i in range(width)]    # x, height

        for b in buildings:
            for x in range(b[0], b[1]):
                if outline[x][1] < b[2]:
                    outline[x][1] = b[2]

        pre_height = outline[0][0]
        skyline = []
        for x in range(width):
            outline[x][0] # x axis
            if pre_height != outline[x][1]: # height
                skyline.append([x, outline[x][1]])
            pre_height = outline[x][1]

        return skyline


    def getSkyline(self, buildings):
        #events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
        events = sorted([(l, -h, r) for l, r, h in buildings] + list([(r, 0, 0) for l, r, h in buildings]))
        print(events)

        res = [[0, 0]]
        hq = [(0, float("inf"))]

        for l, h, r in events:
            while l >= hq[0][1]:    # the heightest height's right side-index
                heapq.heappop(hq)   # the case there is no overlapping area
            heapq.heappush(hq, (h, r))

            if res[-1][1] + hq[0][0]:   # [1] is height
                res += [l, -hq[0][0]],

            print(hq)
            print(res)
            print()
        return res[1:]


# Li, Ri, Hi
#     Li: x axis coordinate
#     Ri: x axis coordinate
#     Hi: height


#buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12]]

stime = time.time()
sol = Solution()
ret = sol.getSkyline(buildings)
print('1: {} sec'.format(time.time() - stime))
print(ret)