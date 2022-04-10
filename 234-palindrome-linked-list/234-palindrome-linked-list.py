# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.helper([head],head,0,[0])
    
    def helper(self,left_ptr,cur,depth,listLen):
        listLen[0] = depth
        if cur is None:
            return True
        if not self.helper(left_ptr,cur.next,depth+1,listLen):
            return False
        if depth >= listLen[0]/2:
            old_left = left_ptr[0]
            left_ptr[0] = left_ptr[0].next
            return cur.val==old_left.val
        else:
            return True
        