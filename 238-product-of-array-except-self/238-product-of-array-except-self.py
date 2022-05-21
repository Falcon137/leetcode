class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [-1 for el in nums]
        comp = [-1 for el in range((len(nums)*2) - 1)]
        self.gen_comp(nums,comp)
        self.process_comp(answer,comp)
        return answer
    
    def gen_comp(self,nums,comp):
        """
        running = nums[0]
        comp = [1]
        for el in nums[1:]:
            comp = [(comp,el),running]
            running *= el
        return comp
        """
        running = nums[0]
        comp_idx = 0
        comp[comp_idx] = 1
        comp_idx += 1
        for el in nums[1:]:
            comp[comp_idx] = el
            comp_idx += 1
            comp[comp_idx] = running
            comp_idx += 1
            running *= el
    
    def process_comp(self,answer,comp):
        """
        factor = 1
        for i in range(len(answer)-1,0,-1):
            answer[i] = comp[1]*factor
            comp,new_factor = comp[0]
            factor *= new_factor
        answer[0] = factor
        """
        factor = 1
        comp_idx = len(comp)-1
        for i in range(len(answer)-1,0,-1):
            answer[i] = comp[comp_idx]*factor
            comp_idx -= 1
            new_factor = comp[comp_idx]
            comp_idx -= 1
            factor *= new_factor
        answer[0] = factor
            
            
            
        
        