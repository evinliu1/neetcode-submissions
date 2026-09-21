class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = {}
        for num in nums:
            ct[num] = ct.get(num, 0) + 1
        
        heap = []
        for num in ct:
            heapq.heappush(heap, (ct[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res