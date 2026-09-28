class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in mp:
                return [mp[num], i]
            mp[diff] = i
        