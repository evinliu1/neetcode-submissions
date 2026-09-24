class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        max_len = 0
        for num in nums:
            if not num_map[num]:
                num_map[num] = num_map[num - 1] + num_map[num + 1] + 1
                num_map[num - num_map[num - 1]] = num_map[num]
                num_map[num + num_map[num + 1]] = num_map[num]
                max_len = max(max_len, num_map[num])
        return max_len

