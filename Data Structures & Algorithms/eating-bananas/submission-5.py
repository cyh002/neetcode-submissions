class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        # 2. Feasibility helper
        def can_finish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h

        # 3. Binary Search over range [low, high]
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_finish(mid):
                ans = mid        # 'mid' works, try to find a smaller speed
                high = mid - 1
            else:
                low = mid + 1    # 'mid' is too slow, must increase speed
                
        return ans
            