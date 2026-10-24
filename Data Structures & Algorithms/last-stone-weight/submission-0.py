import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2, 3, 6, 2, 4]
        # 6, 4 are chosen
        # 6 - 4 = 2
        # [2, 3, 2, 2]
        # 3 - 2 = 1
        # [1, 2, 2]
        # ...
        # [1]
        # Why Heapify? 
        # because we are looking to get the kth first and second. 
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            new = first - second
            heapq.heappush(stones, -new)
        return -stones[0]            
        