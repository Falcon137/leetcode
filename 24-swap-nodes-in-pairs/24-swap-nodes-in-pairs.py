# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head,None)
    
    def helper(self,cur,prev):
        if cur is None:
            return prev
        if prev is None:
            return self.helper(cur.next,cur)
        else:
            aft = cur.next
            cur.next = prev
            prev.next = self.helper(aft,None)
            return cur
        
        