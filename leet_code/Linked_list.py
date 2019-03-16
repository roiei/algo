
class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.pre = None
            self.next = None

    def __init__(self):
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.pre = None
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = None
        self.n = 0

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while self.tail != cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        self.n += 1
        return None

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.n += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        cur = self.head.next
        while self.tail != cur:
            if i == index:
                available = True
                break
            cur = cur.next
            i += 1

        if index == self.n:
            available = True

        if False == available:
            return None

        node = self.Node(val)
        node.pre = cur.pre
        node.next = cur
        cur.pre.next = node
        cur.pre = node
        self.n += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if self.n == 0:
            return None
        i = 0
        available = False
        cur = self.head.next
        while self.tail != cur:
            if i == index:
                available = True              
                break
            cur = cur.next
            i += 1
        if False == available:
            return None
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        self.n -= 1
        return None

    def traverse(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.val, end=' -> ')
            cur = cur.next
        print()

linkedList = MyLinkedList();
print('adding @ head 56')
linkedList.addAtHead(56);
linkedList.traverse()

print('get @ index 1')
print(linkedList.get(1));

print('adding @ 1 50')
linkedList.addAtIndex(1, 50);
linkedList.traverse()

print('deleting @ 1')
linkedList.deleteAtIndex(1);
linkedList.traverse()

print('get @ index 1')
print(linkedList.get(1));

print('adding @ 1 43')
linkedList.addAtIndex(1, 43);
linkedList.traverse()

print('adding @ head 82')
linkedList.addAtHead(82);

print('get @ index 2')
print(linkedList.get(2));

print('deleting @ 3')
linkedList.deleteAtIndex(3);

print('get @ index 1')
print(linkedList.get(1));

