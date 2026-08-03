class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 8
        pre = 1
        res = [1] * (len(nums))
        # [ 1 , 1 , 2, 8]
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        # [ 1 , 1 , 2, 8]
        #              ^looking here
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]

        return res