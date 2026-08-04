class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[r]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                break
            
            mid = (l + r) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return res