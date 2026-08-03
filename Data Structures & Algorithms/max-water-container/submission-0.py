class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            minVal = min(heights[l], heights[r])
            maxVal = distance * minVal
            res = max(res, maxVal)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res