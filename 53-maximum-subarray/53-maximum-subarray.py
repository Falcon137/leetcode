class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -1
        cur_start = -1
        best = nums[0]
        for i,n in enumerate(nums):
            if cur_sum > 0:
                cur_sum += n
            else:
                cur_start = i
                cur_sum = n
            best = max(best,cur_sum)
        return best
                
            
        