class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        for i in range(len(nums)):
            # [ [-1 ]    ,    [0,1,2,-1,-4]   ]
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return res