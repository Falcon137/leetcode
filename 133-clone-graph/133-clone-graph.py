"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        h = {}
        return self.helper(node,h)
    def helper(self,node,h):
        if node in h:
            return h[node]
        h[node] = Node(node.val,[])
        for neigh in node.neighbors:
            h[node].neighbors.append(self.helper(neigh,h))
        return h[node]
            
        
        
        