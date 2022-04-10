class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for el in nums:
            if el in h:
                return True
            h[el] = 'literally_anything'
        return False
                
        