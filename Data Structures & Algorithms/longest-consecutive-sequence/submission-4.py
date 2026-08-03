class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        ct = defaultdict(int)

        for num in nums:
            if not ct[num]:
                ct[num] = ct[num + 1] + ct[num - 1] + 1
                ct[num - ct[num - 1]] = ct[num]
                ct[num + ct[num + 1]] = ct[num]
            res = max(res, ct[num])
        return res