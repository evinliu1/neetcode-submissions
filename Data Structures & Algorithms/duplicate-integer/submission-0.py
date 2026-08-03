class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptySet = set()
        for num in nums:
            if num not in emptySet:
                emptySet.add(num)
            else:
                return True
        return False