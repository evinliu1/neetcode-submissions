class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarifying questions
        # is the list of nums always sorted?
        # will there be ties?
        # how do we handle tie breakers?

        # brute force approach 
        # create a dict of each number and how many times it appears
        # loop through the dict k times

        ct = defaultdict(int)
        for num in nums:
            ct[num] += 1

        arr = []
        for num, ct in ct.items():
            arr.append([ct, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res