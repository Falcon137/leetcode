# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for idx,l in enumerate(lists):
            if l:
                heapq.heappush(h,(l.val,idx))
                l = l.next
        if not h:
            return None
        first,idx = heapq.heappop(h)
        head = tail = ListNode(first)
        lists[idx] = lists[idx].next
        if lists[idx]:
            heapq.heappush(h,(lists[idx].val,idx))
        while h:
            best,idx = heapq.heappop(h)
            tail.next = ListNode(best)
            tail = tail.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(h,(lists[idx].val,idx))
        return head
            
            
        