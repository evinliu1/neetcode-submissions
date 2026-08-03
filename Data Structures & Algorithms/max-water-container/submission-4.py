class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = -1
        
        l = 0 
        r = len(heights) - 1

        while l < r:
            distance = r - l
            minval = min(heights[l],heights[r])
            volume = minval * distance
            res = max(res, volume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res