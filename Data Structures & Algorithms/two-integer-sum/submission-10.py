class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            lookup = target - num
            if lookup not in num_dict:
                num_dict.update({num: i})
            else:
                return sorted([i, num_dict[lookup]])