# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self,root,other):
        if root is None and other is None:
            return True
        elif root is None or other is None:
            return False
        if root.val == other.val:
            return self.sameTree(root.left,other.left) and self.sameTree(root.right,other.right)
        else:
            return False

    
    def helper(self,root,other):
        if root is None:
            return False
        if (root.hash == other.hash) and self.sameTree(root,other):
            return True
        return self.isSubtree(root.left,other) or self.isSubtree(root.right,other)
        
    def get_hashes(self,node):
        if node is None:
            return 0
        node.hash = hash(self.get_hashes(node.left)+self.get_hashes(node.right)+node.val)
        return node.hash
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        self.get_hashes(root)
        self.get_hashes(subRoot)
        return self.helper(root,subRoot)

        