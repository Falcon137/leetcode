class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = {}
        visited = {}
        adjL = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adjL[b].append(a)
        for i in range(numCourses):
            if i not in visited:
                if self.dfs(i,path,adjL,visited)==False:
                    return False
        return True
    
    def dfs(self,node_idx,path,adjL,visited):
        if node_idx in path:
            return False
        if node_idx in visited:
            return True
        path[node_idx] = True
        visited[node_idx] = True
        for neighbor in adjL[node_idx]:
            if self.dfs(neighbor,path,adjL,visited) == False:
                return False
        del path[node_idx]
        return True
        