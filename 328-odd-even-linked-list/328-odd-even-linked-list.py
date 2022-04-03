# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        tail = head
        while tail.next is not None:
            tail = tail.next
        return self.helper(head,tail,tail,True)
    def helper(self,cur,tail,original_tail,isEven):
        if isEven:
            if cur != original_tail:
                cur.next = self.helper(cur.next,tail,original_tail,False)
            return cur
        else:
            if (cur == original_tail) and (cur.next is None):
                return cur
            next_it = cur.next
            cur.next = None
            tail.next = cur
            tail = tail.next
            if cur == original_tail:
                return next_it
            else:
                return self.helper(next_it,tail,original_tail,True)
            
        