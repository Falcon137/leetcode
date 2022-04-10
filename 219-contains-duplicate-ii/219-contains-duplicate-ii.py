class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for idx,val in enumerate(nums):
            if val in h:
                if idx-h[val] <= k:
                    return True
            h[val] = idx
        return False