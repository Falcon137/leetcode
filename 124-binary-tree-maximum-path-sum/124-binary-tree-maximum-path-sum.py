# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val
        self.helper(root)
        return self.best
    def helper(self,node):
        if node is None:
            return 0
        left_best = self.helper(node.left)
        right_best = self.helper(node.right)
        cur_path_value = node.val + max(left_best,0) + max(right_best,0)
        self.best = max(self.best, cur_path_value)
        return node.val + max(max(left_best,right_best),0)