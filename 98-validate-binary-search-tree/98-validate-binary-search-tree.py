# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,None,None)
    
    def helper(self,node,upper,lower):
        if node is None:
            return True
        if node.left:
            if node.left.val >= node.val:
                return False
            if lower and (node.left.val <= lower):
                return False
        if node.right:
            if node.right.val <= node.val:
                return False
            if upper and (node.right.val >= upper):
                return False
        return self.helper(node.left,node.val,lower) and self.helper(node.right,upper,node.val)
                
                 
           
        
        