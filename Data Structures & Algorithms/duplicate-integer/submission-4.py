class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1,2,3,3]
        # is there any case that it won't have a duplicate? if so return -1
        
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False