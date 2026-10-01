class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv, l , r = 0, 0, len(heights) - 1

        while l < r:
            lheight, rheight = heights[l], heights[r]
            height = min(lheight, rheight)
            vol = height * (r - l)
            maxv = max(maxv, vol)
            if lheight < rheight:
                l += 1
            else:
                r -= 1
        return maxv