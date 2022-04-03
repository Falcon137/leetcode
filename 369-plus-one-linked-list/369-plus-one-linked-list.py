# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if self.addOne(head):
            return ListNode(1,head)
        return head
    
    def addOne(self,head):
        if head is None:
            return True
        head.val = head.val + (1 if self.addOne(head.next) else 0)
        if head.val == 10:
            head.val = 0
            return True
        return False
        