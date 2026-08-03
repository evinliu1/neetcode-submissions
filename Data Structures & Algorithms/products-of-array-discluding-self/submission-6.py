class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # [ 1  2  4  6 ]
    # pre [ 1  1  1  1 ]
    # post[ 1  1  1  1 ]
        # [ 1  1  1  1 ]

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre

        
        print(res)

        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = post * res[i]
            post = nums[i] * post

        return res