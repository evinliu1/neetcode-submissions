class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [ 1 2 2 3 3 3 4 ]
        # find count
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        '''
        count = {
            1: 1
            2: 2
            3: 3
            4: 1
        }
        '''
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # heap = [ (2, 2) (3, 3)]
        #           num  ct
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res