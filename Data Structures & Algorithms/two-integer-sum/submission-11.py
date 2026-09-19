class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] t = 7
        # will we always be able to find a solution ? return [-1, -1] if so
        # are we returning the indices or the numbers themselves ?

        # brute force approach
        # double for loop checking if each number adds up to target
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        continue
                    return [i, j]
        
