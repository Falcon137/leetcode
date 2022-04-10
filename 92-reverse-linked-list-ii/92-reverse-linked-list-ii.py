# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        revLen = (right-left)+1
        cur = dummy
        pos = 0
        while pos < left-1:
            cur = cur.next
            pos += 1
        cur.next = self.revSection(cur.next,revLen)
        return dummy.next
    
    def revSection(self,first,revLen):
        cur = first
        prev = None
        temp = None
        pos = 0
        while pos < revLen:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            pos += 1
        first.next = cur
        return prev