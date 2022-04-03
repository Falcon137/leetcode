# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        listLen = 0
        cur = head
        while cur is not None:
            listLen += 1
            cur = cur.next
        k = k%listLen
        if k == 0:
            return head
        target = listLen -1 - k
        new_head,new_tail = self.helper(head,target,0)
        new_tail.next = head
        return new_head
    
    def helper(self,cur,target,idx):
        if idx == target:
            cap = cur.next
            cur.next = None
            new_tail = cap
            while new_tail.next is not None:
                new_tail = new_tail.next
            return (cap,new_tail)
        else:
            return self.helper(cur.next,target,idx+1)
            
        