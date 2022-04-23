class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for n in nums:
            if n not in h:
                h[n] = 'a'
            else:
                return True
        return False
                
        