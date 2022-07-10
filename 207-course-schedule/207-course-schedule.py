class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjL = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adjL[b].append(a)
        visited = {}
        trap = {}
        for i in range(numCourses):
            if i not in visited:
                if self.dfs(i,visited,adjL,trap):
                    return False
        return True
    
    def dfs(self,i,visited,adjL,trap):
        if i in visited:
            trap[i] = True
            return False
        visited[i] = True
        for neighbor in adjL[i]:
            if self.dfs(neighbor,visited,adjL,trap):
                return True
        if i in trap:
            return True
        return False
            