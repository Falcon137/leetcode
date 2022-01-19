class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_index = 0
        right_index = n-1
        best = 0
        while left_index < right_index:
            candidate = min(height[left_index],height[right_index])*(right_index-left_index)
            best = max(best,candidate)
            if height[left_index] <= height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return best
            
        