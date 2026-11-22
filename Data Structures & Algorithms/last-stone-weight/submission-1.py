import heapq
class Solution:
    # default is minheap
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            first = -heapq.heappop(neg_stones)
            second = -heapq.heappop(neg_stones)
            diff = first - second
            heapq.heappush(neg_stones, -diff)
        return -neg_stones[0] 
            

                