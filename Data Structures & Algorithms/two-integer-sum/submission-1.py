class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        return

        # [ 1 , 2 , 3, 4 , 5] target = 7
        # 7 - 5 = 2
        # look for prevMap[2] -> returns 1
        # return [1, 4]
        """
        dict -> {
            1 : 0
            2 : 1
            3 : 2
            4 : 3
            5 : 4
        }
        """
