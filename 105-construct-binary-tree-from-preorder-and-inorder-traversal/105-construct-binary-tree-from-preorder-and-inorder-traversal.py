# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mapping = {el:i for i,el in enumerate(inorder)}
        self.preorder = preorder
        self.inorder = inorder
        inorder_pos = [0]
        return self.helper(0,len(preorder),inorder_pos)
    def helper(self,l,r,pos):
        if r-l == 0:
            pos[0] -= 1
            return None
        parent = TreeNode(self.preorder[pos[0]])
        mid = self.mapping[self.preorder[pos[0]]]
        pos[0] += 1
        parent.left = self.helper(l,mid,pos)
        pos[0] += 1
        parent.right = self.helper(mid+1,r,pos)
        return parent