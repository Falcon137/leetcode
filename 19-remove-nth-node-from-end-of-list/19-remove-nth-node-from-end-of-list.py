# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        cur = head
        while cur is not None:
            listLen += 1
            cur = cur.next
        target = listLen - n
        return self.removeTarget(head,target,0)
    def removeTarget(self,head,target,idx):
        if head is None:
            return None
        if target == idx:
            return self.removeTarget(head.next,target,idx+1)
        head.next = self.removeTarget(head.next,target,idx+1)
        return head
        
        