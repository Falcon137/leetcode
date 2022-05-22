# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(0,root)])
        stuff = []
        while q:
            level,cur = q.popleft()
            stuff.append((level,cur.val))
            if cur.left:
                q.append((level+1,cur.left))
            if cur.right:
                q.append((level+1,cur.right))
        out = []
        for level,val in stuff:
            if level == len(out):
                out.append([])
            out[-1].append(val)
        return out
            
            
            
            