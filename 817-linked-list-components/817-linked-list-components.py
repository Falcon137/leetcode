# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        inComponent = False
        cur = head
        componentCount = 0
        h = {k:True for k in nums}
        while cur:
            if (not inComponent) and (cur.val in h):
                componentCount += 1
                inComponent = True
            if inComponent and (cur.val not in h):
                inComponent = False
            cur = cur.next
        return componentCount
                
                
            
            
        