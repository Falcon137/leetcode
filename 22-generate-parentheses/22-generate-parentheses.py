from queue import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = self.helper(n)
        return [k[0] for k in out[n]]
    
    def helper(self,n):
        if n==0:
            return [[('',0)]]
        sub_problems = self.helper(n-1)
        q = Queue(maxsize=0)
        q.put(('',0))
        new_guys = []
        while not q.empty():
            cur = q.get()
            if cur[1] == n:
                new_guys.append(cur)
            else:
                needed = n-cur[1]
                for i in range(needed):
                    for pattern,num in sub_problems[i]:
                        new_pattern = cur[0]+'('+pattern+')'
                        new_num = cur[1]+num+1
                        q.put((new_pattern,new_num))
        sub_problems.append(new_guys)
        return sub_problems
                        
                        
        
        
        