class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarifying questions
        # is the list of nums always sorted?
        # will there be ties?
        # how do we handle tie breakers?

        # brute force approach 
        # create a dict of each number and how many times it appears
        # loop through the dict k times

        # ct = defaultdict(int)
        # for num in nums:
        #     ct[num] += 1

        # ct = sorted(ct.items(), key=lambda items: items[1])
        # res = []
        # for _ in range(k):
        #     res.append(ct.pop()[0])
        # return res

        # faster approach is to use a minheap
        ct = {}
        for num in nums:
            ct[num] = ct.get(num, 0) + 1
        
        heap = []
        for num in ct.keys():
            heapq.heappush(heap, (ct[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
