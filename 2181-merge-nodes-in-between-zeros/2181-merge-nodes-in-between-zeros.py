# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head.next = self.helper(head.next,0)
        return head.next
    
    def helper(self,cur,agg):
        if cur is None:
            return None
        if cur.val != 0:
            agg += cur.val
            return self.helper(cur.next,agg)
        else:
            if agg == 0:
                cur.next = self.helper(cur.next, 0)
                return cur
            else:
                agg_node = ListNode(agg)
                agg_node.next = self.helper(cur.next,0)
                return agg_node
        