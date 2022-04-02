# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        return self.helper(head,stack,True)
    
    def helper(self,cur,stack,left):
        if cur == stack[-1]:
            cur.next = None
            return cur
        elif left:
            next_guy = cur
            cur = cur.next
            next_guy.next = self.helper(cur,stack,False)
            return next_guy
        else:
            next_guy = stack.pop()
            next_guy.next = self.helper(cur,stack,True)
            return next_guy
        