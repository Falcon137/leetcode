# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        r1 = head.next
        r2 = head.next.next
        while r1 and r2:
            if r1 == r2:
                break
            r1 = r1.next
            r2 = None if r2.next is None else r2.next.next
        if r1 is None or r2 is None:
            return None
        h = {r1:True}
        r3 = r1.next
        while r3 != r1:
            h[r3] = True
            r3 = r3.next
        r4 = head
        pos = 0
        while r4 not in h:
            r4 = r4.next
            pos += 1
        return r4
            
        
        