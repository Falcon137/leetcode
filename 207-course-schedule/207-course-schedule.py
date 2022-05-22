class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjL = {i:[] for i in range(numCourses)}
        dependencies = [0 for _ in range(numCourses)]
        print(adjL)
        print(dependencies)
        for p in prerequisites:
            a,b = p[0],p[1]
            adjL[b].append(a)
            dependencies[a] += 1
        
        available = []
        for idx,d in enumerate(dependencies):
            if d == 0:
                available.append(idx)
            
        while available:
            k = available.pop()
            targets = adjL[k]
            for t in targets:
                dependencies[t] -= 1
                if dependencies[t] == 0:
                    available.append(t)
                    
        for d in dependencies:
            if d != 0:
                return False
        return True
            
        
        