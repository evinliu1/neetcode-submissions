class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #   1 2 3 3 3 3
        #   k = 2

        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        heap = []
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res