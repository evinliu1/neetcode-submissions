class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = defaultdict(int)
        length = 0

        for num in nums:
            if count[num] == 0:
                count[num] = count[num - 1] + count[num + 1] + 1
                count[num - count[num - 1]] = count[num]
                count[num + count[num + 1]] = count[num]
                length = max(length, count[num])
        print(count)
        return length
