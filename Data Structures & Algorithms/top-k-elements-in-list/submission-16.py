class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1

        max_heap = [(-freq, num) for num, freq in count_dict.items()]
        heapq.heapify(max_heap)
        
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
        