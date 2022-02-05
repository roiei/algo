
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class LinkedList:
    def __init__(self, size):
        self.size = size
        self.num = 0
        self.head = Node(None)

    def insert(self, value) -> bool:
        if self.num >= self.size:
            return False

        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.num += 1
        return True

    def traverse(self):
        cur = self.head.next

        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value):
        pre = self.head
        cur = self.head.next

        while cur:
            if cur.data == value:
                pre.next = cur.next
                self.num -= 1
                return True
            pre = cur
            cur = cur.next

        return False


def test_sll():
    linked_list = LinkedList(3)

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.traverse()
    linked_list.remove(3)
    linked_list.traverse()


class DoubleLinkedList:
    def __init__(self, size):
        self.size = size
        self.num = 0        
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self, value):
        if self.num >= self.size:
            return False

        node = Node(value)

        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
        self.num += 1
        return True

    def traverse(self):
        cur = self.head.next

        while cur != self.tail:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value):
        cur = self.head.next

        while cur != self.tail:
            if cur.data == value:
                cur.next.pre = cur.pre
                cur.pre.next = cur.next
                self.num -= 1
                return True
            cur = cur.next

        return False

    def removeAtLast(self):
        if self.num == 0:
            return None

        node = self.tail.pre
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        self.num -= 1
        return node


def test_dll():
    linked_list = DoubleLinkedList(3)

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.traverse()
    node = linked_list.removeAtLast()
    print(node.data)
    linked_list.traverse()

test_dll()