import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 10 bananas 
        # [1, 4, 3, 2]
        # 9 hours. deadline
        # k : eating rate 
        # for eating rate of 2 : 1, 2, 2, 1 = 6
        # for eating rate of 1 : 1, 4, 3, 2 = 10

        # Why is this a binary search question 
        # this is because we are searching via a list of answers

        low = 1
        high = max(piles)
        ans = high # start with the highest

        # feasibility helper
        def can_finish(speed, h):
            hours = 0 
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
        
        while low <= high: 
            mid = low + (high - low) // 2
            if can_finish(mid, h):
                # print(f"speed : {mid}, finished. ")
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 

        return ans
        



