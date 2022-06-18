class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = [False]*n
        adjL = [[] for _ in range(n)]
        for e in edges:
            a,b = e[0],e[1]
            adjL[a].append(b)
            adjL[b].append(a)
        cc = 0
        for i in range(n):
            if not seen[i]:
                cc += 1
                self.dfs(i,adjL,seen)
                
        return cc
    
    def dfs(self,i,adjL,seen):
        seen[i] = True
        for neigh in adjL[i]:
            if not seen[neigh]:
                self.dfs(neigh,adjL,seen)
        
            
            
            
        