class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len({i:True for i in nums})!=len(nums)
                
        