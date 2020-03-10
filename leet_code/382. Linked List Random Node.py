class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.data = []
        node = head
        while node:
            self.data += node.val,
            node = node.next
        self.n = len(self.data)

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        idx = random.randint(0, self.n-1)
        return self.data[idx]