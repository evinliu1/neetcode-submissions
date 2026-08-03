class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
            #       #
            #       #   #
            #   #   #   #
            #   # # #   #
            #   # # # # #
            # # # # # # #
          # # # # # # # #
    #     1 7 2 5 4 7 3 6
    #     ^ ^           ^
    # minheight = 1
    # maxcontainer = 7

        # keep track of distance between pointers
        # keep track of max container
        # keep track of min between pointers

        l = 0
        r = len(heights) - 1
        res = 0 # max container

        while l < r:
            minHeight = min(heights[l], heights[r])
            distance = r - l
            container = minHeight * distance
            res = max(res, container)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        