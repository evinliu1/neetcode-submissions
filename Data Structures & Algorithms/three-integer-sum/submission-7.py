class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                print(f'\nnums[i]: {nums[i]}\nnums[l]: {nums[l]}\nnums[r]:{nums[r]}\n')
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        print(res)
        return res