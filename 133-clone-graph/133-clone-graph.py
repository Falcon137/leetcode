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
        self.load_hashmap(node,h)
        h2 = {}
        self.copy_verticies(node,h,h2)
        return h[node]
    
    def load_hashmap(self,node,h):
        h[node] = Node(node.val)
        for neigh in node.neighbors:
            if neigh not in h:
                self.load_hashmap(neigh,h)
    
    def copy_verticies(self,node,h,h2):
        h2[node] = True
        for neigh in node.neighbors:
            h[node].neighbors.append(h[neigh])
        
        for neigh in node.neighbors:
            if neigh not in h2:
                self.copy_verticies(neigh,h,h2)
            
        
        
        