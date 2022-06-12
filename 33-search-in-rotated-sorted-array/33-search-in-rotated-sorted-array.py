class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(0,len(nums),nums,target)
    
    def helper(self,start,stop,nums,target):
        if (stop - start) == 0:
            return -1
        mid = start + (stop-start)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]: #one element case falls here
            if nums[start] <= target and target <= nums[mid]:
                return self.helper(start,mid,nums,target)
            else:
                return self.helper(mid+1,stop,nums,target)
        else:
            if nums[mid] <= target and target <= nums[stop-1]:
                return self.helper(mid+1,stop,nums,target)
            else:
                return self.helper(start,mid,nums,target)
                
        
        