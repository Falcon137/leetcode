from functools import reduce
class Solution:
    def product(self,nums):
        if len(nums)==0:
            return -1
        return reduce((lambda x,y: x*y),nums)
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        for i,n in enumerate(nums):
            if n == 0:
                return max(max(self.maxProduct(nums[:i]),self.maxProduct(nums[i+1:])),0)
            
        neg_count = 0
        first_neg = -1
        last_neg = -1
        for i,n in enumerate(nums):
            if n < 0:
                neg_count += 1
                last_neg = i
                if first_neg == -1:
                    first_neg = i
        
        if neg_count%2 == 0:
            return self.product(nums)
        else:
            return max(self.product(nums[:last_neg]),self.product(nums[first_neg+1:]))
        