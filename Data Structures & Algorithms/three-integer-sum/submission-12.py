class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            print(f"i: {nums[i]}, l: {nums[l]}, r: {nums[r]}\nthree_sum: {nums[i] + nums[l] + nums[r]}")

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1 
                else:
                    if ([nums[i],nums[l],nums[r]]) not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
        return res