class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = nums[r]

        while l <= r:
            if nums[l] <= nums[r]:
                lowest = min(lowest, nums[l])

            mid = (r - l) + 1 // 2
            lowest = min(lowest, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return lowest