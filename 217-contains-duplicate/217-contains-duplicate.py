class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for el in nums:
            if el in h:
                return True
            h[el] = 'a'
        return False
                
        