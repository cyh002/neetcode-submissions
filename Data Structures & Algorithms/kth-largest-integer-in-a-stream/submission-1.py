import heapq
class KthLargest:

# Goal: we want the smallest among kth 
 
# 1. Convert it into a Min Heap
# 2. Pop until we get have k left in the heap
# 3. then we get the minimum of what is left in the heap 

# Benefits of Heaps:
# heapify process is O(n)
# get the min : O(1)
# 
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            # we need to keep popping
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]        
