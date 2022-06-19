class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = [-1]*n
        adjL = [[] for _ in range(n)]
        for e in edges:
            a,b = e[0],e[1]
            adjL[a].append(b)
            adjL[b].append(a)
        
        cc = 0
        for i in range(n):
            if seen[i] == -1:
                seen[i] = n
                if self.dfs(i,adjL,seen) == False:
                    return False
                cc += 1
        return cc ==1
    
    def dfs(self,i,adjL,seen):
        for neigh in adjL[i]:
            if seen[neigh]==-1:
                seen[neigh]=i
                if self.dfs(neigh,adjL,seen) == False:
                    return False
            elif neigh != seen[i]:
                return False
        return True
        