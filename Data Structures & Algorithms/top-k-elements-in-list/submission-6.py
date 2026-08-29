import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heaps 
        counted = dict(Counter(nums))
        heap = []
        # We build a Min Heap so that we can only leave the largest and remove the Min freq
        for num in counted.keys():
            freq = counted[num]
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = sorted(heap, key = lambda x:-x[1])
        return [tup[1] for tup in result]

