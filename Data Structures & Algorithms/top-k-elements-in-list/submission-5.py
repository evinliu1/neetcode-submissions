class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums : 1 1 2 2 2 3 3 3 3 4
        # k = 2

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        '''
        {
            1 : 2
            2 : 3
            3 : 4
            4 : 1
        }
        '''

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        '''
        [(3,2), (4,3)]
        '''

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
