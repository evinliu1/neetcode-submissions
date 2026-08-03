class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            shortest = min(heights[l],heights[r])
            distance = r - l
            volume = shortest * distance
            res = max(volume, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res