class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result_init = 0

        while left < right:
            result = min(heights[left], heights[right]) * (right - left)
            result_init = max(result_init, result)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result_init
