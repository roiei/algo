import collections
import bisect


def search(items, item):
    r = len(items) - 1
    l = 0

    while l <= r:
        m = (l + r)//2
        if items[m][0] == item[0]:
            return m
        if items[m][0] < item[0]:
            l = m + 1
        else:
            r = m - 1

    return l


class Solution:
    def meetingRoomIII(self, intervals, rooms, ask):
        intervals.sort()
        res = []

        for item in ask:
            idx = search(intervals, item)

            if intervals[idx][0] == item[0]:
                res += False,
                continue

            if idx > 0 and intervals[idx - 1][1] > item[0] and \
                intervals[idx - 1][0] < item[1]:
                res += False,
                continue

            if idx < len(intervals) - 1 and intervals[idx + 1][0] < item[1] and \
                item[0] < intervals[idx + 1][1]:
                res += False,
                continue

            res += True,

        return res


#print(2 == Solution().canAttendMeetings(get_intervals([(0,30),(5,10),(15,20)])))
#print(1 == Solution().canAttendMeetings(get_intervals([(2, 7)])))
print([True,True] == Solution().meetingRoomIII([[1,2],[4,5],[8,10]], 1, [[2,3],[3,4]]))

