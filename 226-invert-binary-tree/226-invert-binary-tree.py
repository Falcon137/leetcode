# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        old_left, old_right = root.left, root.right
        root.left = self.invertTree(old_right)
        root.right = self.invertTree(old_left)
        return root
        