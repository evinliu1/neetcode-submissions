class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hmap = defaultdict(int)

        for num in nums:
            # if hmap[num] is a non 0 value
            if not hmap[num]:
                hmap[num] = hmap[num - 1] + hmap[num + 1] + 1
                hmap[num - hmap[num - 1]] = hmap[num]
                hmap[num + hmap[num + 1]] = hmap[num]
                res = max(res, hmap[num])
        
        return res