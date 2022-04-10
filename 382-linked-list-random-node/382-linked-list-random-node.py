# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.my_len = 0
        cur = head
        while cur:
            self.my_len += 1
            cur = cur.next
            
        

    def getRandom(self) -> int:
        r = random.choice(range(self.my_len))
        pos = 0
        cur = self.head
        while pos < r:
            cur = cur.next
            pos += 1
        return cur.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()