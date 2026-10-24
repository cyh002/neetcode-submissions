import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        minNums = nums
        heapq.heapify(minNums)
        while len(minNums) > k:
            heapq.heappop(minNums)
        return minNums[0]
