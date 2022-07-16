class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = {i:False for i in range(numCourses)}
        visited = {i:False for i in range(numCourses)}
        adjL = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adjL[b].append(a)
        for i in range(numCourses):
            if visited[i] == False:
                if self.isCyclic(i,path,adjL,visited):
                    return False
        return True
    
    def isCyclic(self,node_idx,path,adjL,visited):
        if path[node_idx]:
            return True
        if visited[node_idx]:
            return False
        path[node_idx] = True
        visited[node_idx] = True
        for neighbor in adjL[node_idx]:
            if self.isCyclic(neighbor,path,adjL,visited):
                return True
        path[node_idx]=False
        return False
        