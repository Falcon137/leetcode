class Solution:
    class node:
        def __init__(val):
            self.neighbors = []
            self.val = val

    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return None
        adjL = {}
        all_letters = {chr(ord('a')+i):False for i in range(26)}
        for letter in all_letters:
            adjL[letter] = []
        prev = words[0]
        alphabet = {}
        self.alph(prev,alphabet)
        for cur in words[1:]:
            fd = self.get_first_difference(prev,cur)
            if fd >= 0:
                adjL[prev[fd]].append(cur[fd])
            elif len(cur) < len(prev):
                return ''
            self.alph(cur,alphabet)
            prev = cur
        return self.topo_sort(adjL,alphabet)
                
     
    def alph(self,word,alph):
        for letter in word:
            alph[letter] = True
        
    def get_first_difference(self,a,b):
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                return i
        return -1
    
    def topo_sort(self,adjL,alphabet):
        dependencies = {k:0 for k in alphabet}
        for source in adjL:
            for destination in adjL[source]:
                dependencies[destination] +=1 
        
        available = []
        for k in dependencies:
            if dependencies[k] == 0:
                available.append(k)
                
        my_schedule = ''
            
        while available:
            source = available.pop()
            if source in alphabet:
                my_schedule += source
            for d in adjL[source]:
                dependencies[d] -= 1
                if dependencies[d] == 0:
                    available.append(d)
        for a in alphabet:
            if a not in my_schedule:
                return ''
        return my_schedule
        
        
        
                
        
        
        