class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        north = [(0,c) for c in range(cols)]
        east = [(r,cols-1) for r in range(rows)]
        south = [(rows-1,c) for c in range(cols)]
        west = [(r,0) for r in range(rows)]
        
        pacific_hits = {}
        pacific_border = north+west
        for pos in pacific_border:
            if pos not in pacific_hits:
                self.dfs(heights,pos,pacific_hits)
        atlantic_hits = {}
        atlantic_border = south+east
        
        for pos in atlantic_border:
            if pos not in atlantic_hits:
                self.dfs(heights,pos,atlantic_hits)
        
                
        results = []
        for pos in pacific_hits.keys():
            if pos in atlantic_hits:
                results.append(pos)
        return results
    
    
    def get_neighbors(self,heights,pos):
        n = len(heights)
        m = len(heights[0])
        neighbors = []
        r,c = pos
        candidates = [(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
        for a,b in candidates:
            if (a >= 0) and (a < n) and (b >=0) and (b < m):
                neighbors.append((a,b))
        return neighbors
    
    def dfs(self,heights,pos,visited):
        if pos in visited:
            return 
        visited[pos] = True
        for neighbor in self.get_neighbors(heights,pos):
            if heights[neighbor[0]][neighbor[1]] >= heights[pos[0]][pos[1]]:
                self.dfs(heights,neighbor,visited)
        