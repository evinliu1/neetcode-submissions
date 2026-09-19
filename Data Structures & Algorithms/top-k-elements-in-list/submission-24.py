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

        ct = sorted(ct.items(), key=lambda items: items[1])
        res = []
        for _ in range(k):
            res.append(ct.pop()[0])
        return res