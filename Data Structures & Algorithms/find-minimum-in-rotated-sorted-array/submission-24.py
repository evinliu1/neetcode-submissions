class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[r]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (r + l) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res