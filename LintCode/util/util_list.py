

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(numstr):
    nums = list(map(int, numstr.split('->')))
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next
    return head

def create_list(numstr, delimiter):
    nums = list(map(int, numstr.split(delimiter)))
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next
    return head

def list_traverse(list):
    cur = list
    while None != cur:
        print(cur.val)
        cur = cur.next