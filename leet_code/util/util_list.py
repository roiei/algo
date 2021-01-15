

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def create_linked_list(numstr):
    nums = list(map(int, numstr.split('->')))
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next
    return head


def create_linked_list_from_nums(nums):
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next
    return head


def create_circular_linked_list_from_nums(nums):
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next

    cur.next = head
    return head


def list_traverse(list):
    cur = list
    while None != cur:
        print(cur.val)
        cur = cur.next

def list_get_nums(node):
    res = []
    while node:
        res += node.val,
        node = node.next
    return res


def list_is_same_list(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return l1 == None and l2 == None

