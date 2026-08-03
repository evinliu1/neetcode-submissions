class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [ 1 ] * len(nums)

        # [ 1 1 1 1 ]

        before = 1
        for i in range(len(nums)):
            res[i] = before
            before = nums[i] * before

        after = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = after * res[i]
            after = after * nums[i]
        
        return res