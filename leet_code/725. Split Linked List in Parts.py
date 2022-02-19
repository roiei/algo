
import time
from util.util_list import *


class Solution:
    def split_linked_list(self, head, k):
        if not head:
            return [None for _ in range(k)]

        nodes = []
        while head:
            nodes += head,
            head = head.next

        n = len(nodes)
        part = n // k
        remainder = n % k

        i = 0
        chunks = []

        while i < n:
            until = i + part
            chunks += nodes[i],

            while i < until and i < n:
                i += 1

            if i < n and remainder:
                remainder -= 1
                i += 1

            nodes[i - 1].next = None

        while chunks and len(chunks) < k:
            chunks += None,

        return chunks


# chunks = split_linked_list(create_linked_list_from_nums([1,2,3,4,5,6,7,8]), 3)
# for chunk in chunks:
#     print(list_get_nums(chunk))

stime = time.time()
chunks = Solution().splitListToParts(create_linked_list_from_nums([1,2,3,4,5,6,7,8]), 3)
for chunk in chunks:
    print(list_get_nums(chunk))
#print(Solution().splitListToParts(create_linked_list_from_nums([1, 2, 3]), 3))
#print(Solution().splitListToParts(create_linked_list_from_nums([]), 3))
print('elapse time: {} sec'.format(time.time() - stime))
