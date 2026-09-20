class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # double loop
        # check the product of every value aside from itself and place it in the proper index of res array
        
        # # initialize a list of len nums
        # res = [0] * len(nums) # [0, 0, 0, 0]

        # for i in range(len(nums)): # [ [1] , 2, 4, 6]
        #     running_mult = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         running_mult *= nums[j]    
        #     res[i] = running_mult
        # return res

        # optimal
        # 2x single loop
        # calculate the prefix values moving forwards while updating res array
        # calculate the postfix values while moving backwards while updating res array
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)): # [ 1 , 2 , 4 , 6] - > [ 1 , 1 , 2 , 8]
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # [ 1 , 2 , 4 , 6]
        for i in range(len(nums) - 1, -1, -1): # [ 1 , 1 , 2 , [8]] -> [ [48 , 24 , 12] , 8] - postfix : 1 -> 6 - > 24 - > 48
            res[i] *= postfix
            postfix *= nums[i]

        return res












