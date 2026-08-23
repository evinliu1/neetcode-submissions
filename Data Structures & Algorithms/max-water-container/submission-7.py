class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            vol = height * width
            max_vol = max(vol, max_vol)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_vol