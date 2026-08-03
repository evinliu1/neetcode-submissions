class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
        
        max_heap = [ (-freq, num) for num, freq in num_count.items()]
        heapq.heapify(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(k)]