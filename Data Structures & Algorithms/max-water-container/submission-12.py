class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv, l , r = 0, 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            vol = height * (r - l)
            maxv = max(maxv, vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxv