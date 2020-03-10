
import time


class MyCalendar:
    def __init__(self):
        self.books = []
        self.n = 0

    def book(self, start: int, end: int) -> bool:
        if not (start < end):
            return False
        insertable = True
        for b in self.books:
            if b[0] >= end or b[1] <= start:
                continue
            insertable = False
            break
        if True == insertable:
            self.books.append([start, end])
            self.n += 1
        return insertable


stime = time.time()

bookings = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
expected = [True,True,False,False,True,False,True,True,True,False]

bookings = [[10, 20], [15, 25], [20, 30]]
expected = [True, False, True]

mc = MyCalendar();
res = []
for booking in bookings:
    res.append(mc.book(booking[0], booking[1]));
print(expected)
print(res)
if expected == res:
    print('Okay')
else:
    print('Error')

print('elapse time: {} sec'.format(time.time() - stime))
