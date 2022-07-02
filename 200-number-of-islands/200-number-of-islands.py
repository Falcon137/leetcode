class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        h = {}
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if (r,c) not in h and grid[r][c]=='1':
                    self.dfs(r,c,grid,num_rows,num_cols,h)
                    num_islands += int(grid[r][c])
        return num_islands
    
    def dfs(self,r,c,grid,num_rows,num_cols,h):
        if (r,c) in h:
            return
        h[(r,c)] = True
        for new_r,new_c in self.get_neighbors(r,c,num_rows,num_cols,grid):
            self.dfs(new_r,new_c,grid,num_rows,num_cols,h)
            
    def get_neighbors(self,r,c,num_rows,num_cols,grid):
        neighbors = []
        potential_neighbors = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]
        for p_r,p_c in potential_neighbors:
            if p_r >= 0 and p_r < num_rows and p_c >=0 and p_c < num_cols:
                if grid[p_r][p_c] == grid[r][c]:
                    neighbors.append((p_r,p_c))
        return neighbors
        
        
                    
        