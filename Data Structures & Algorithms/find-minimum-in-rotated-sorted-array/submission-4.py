class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = max(nums)

        # [ 3 4 5 6 | 1 2 ]
        #   L   M       R

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            m = ( l + r ) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res

