class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = [False]*n
        adjL = [[] for _ in range(n)]
        for e in edges:
            a,b = e[0],e[1]
            adjL[a].append(b)
            adjL[b].append(a)
        
        cc = 0
        for i in range(n):
            if seen[i] == False:
                if cc > 0:
                    return False
                seen[i] = True
                if self.dfs(i,adjL,seen,n) == False:
                    return False
                cc += 1
        return True
    
    def dfs(self,i,adjL,seen,prev):
        for neigh in adjL[i]:
            if not seen[neigh]:
                seen[neigh] = True
                dfs = self.dfs(neigh,adjL,seen,i)
                if dfs == False:
                    return False
            elif (neigh != prev):
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        