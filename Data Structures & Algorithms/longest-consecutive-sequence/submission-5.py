class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        res = 0
        for num in nums:
            if not count[num]:
                count[num] = count[num - 1] + count[num + 1] + 1
                count[num - count[num - 1]] = count[num]
                count[num + count[num + 1]] = count[num]
            
            res = max(res, count[num])
        return res