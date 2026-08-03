class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums : 1 2 2 3 3 3 
        # k = 2

        # first get count of each number and save it into a map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        print(count)
        
        # create a heap of key value tuples and pop first in when above k
        heap = []
        # heap = [(2,2), (3,3)]
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
        # res = [2, 3]
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        print(res)
        return res