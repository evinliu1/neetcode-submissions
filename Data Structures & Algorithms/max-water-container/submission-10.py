class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is calculated by the width vs the height
        # the brute force approach is to calculate the areas in a double for loop

        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         max_area = max(max_area, area)
        # return max_area

        # a better approach is to use two pointers 
        # calculate the area while moving inward based on which side has a greater height

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width, height = r - l, min(heights[l], heights[r])
            area = width * height
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area