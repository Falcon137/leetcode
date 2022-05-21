class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stuff = sorted(enumerate(nums),key = lambda x: x[1])
        nums = [el[1] for el in stuff]
        mapping = [el[0] for el in stuff]
        l = 0
        r = len(nums)-1
        while l < r:
            cand = nums[l]+nums[r]
            if cand == target:
                return [mapping[l],mapping[r]]
            elif cand > target:
                r -= 1
            elif cand < target:
                l += 1
        return [-1,-1]
        