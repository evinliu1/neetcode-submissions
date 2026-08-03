class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        res = 0
        for num in nums:
            if not vals[num]:
                vals[num] = vals[num - 1] + vals[num + 1] + 1
                vals[num - vals[num - 1]] = vals[num]
                vals[num + vals[num + 1]] = vals[num]
            res = max(res, vals[num])
        return res