class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dfs brute force solution
        # max_len = 0
        # seen = set()

        # def find_left(num, running_length, seen):
        #     num -= 1
        #     if (num) not in nums:
        #         return running_length
        #     seen.add(num)
        #     return find_left(num, running_length + 1, seen)

        
        # def find_right(num, running_length, seen):
        #     num += 1
        #     if num not in nums:
        #         return running_length
        #     seen.add(num)
        #     return find_right(num, running_length + 1, seen)

        # for num in nums:
        #     if num in seen:
        #         continue
        #     left = find_left(num, 0, seen)
        #     right = find_right(num, 0, seen)
        #     length = left + right + 1
        #     max_len = max(max_len, length)
        #     seen.add(num)
        # return max_len

        # optimal
        # use default dict to check update length in On time
        lengths = defaultdict(int)
        res = 0
        for num in nums:
            if not lengths[num]:
                lengths[num] = lengths[num - 1] + lengths[num + 1] + 1
                lengths[num - lengths[num - 1]] = lengths[num]
                lengths[num + lengths[num + 1]] = lengths[num]
                res = max(res, lengths[num])
        return res


            