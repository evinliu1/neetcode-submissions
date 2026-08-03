class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                threesum = nums[i] + nums[r] + nums[l]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res