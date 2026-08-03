class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#       2 20 4 10 3 4 5
#       ^
#   l = 6
#count= 4
        res = 0

        for num in nums:
            count = 1
            l = num
            while l + 1 in nums:
                l += 1
                count +=1
            res = max(res, count)

        return res