import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq = Counter(nums)

        # Use a heap (min-heap of size k)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract just the numbers
        return [num for count, num in heap]
