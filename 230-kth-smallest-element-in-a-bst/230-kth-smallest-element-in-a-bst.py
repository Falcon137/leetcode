# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, my_guy: Optional[TreeNode], k: int) -> int:
        left_size = self.get_size(my_guy.left)
        right_size = self.get_size(my_guy.right)
        if left_size+1 == k:
            return my_guy.val
        elif k <= left_size:
            return self.kthSmallest(my_guy.left,k)
        else:
            return self.kthSmallest(my_guy.right,k-(left_size+1))
        
        
    def get_size(self,my_guy):
        if my_guy is None:
            return 0
        return 1 + self.get_size(my_guy.left) + self.get_size(my_guy.right)
        