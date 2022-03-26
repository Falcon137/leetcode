# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        r1 = r2 = head
        while (r1 is not None) and (r2 is not None):
            r1 = r1.next
            r2 = None if r2.next is None else r2.next.next
            if r1 == r2:
                return True
        return False
            
        