class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        n = len(prices)
        max_p = 0
        for i in range(n):
            for j in range(i,n):
                p = prices[j] - prices[i]
                max_p = max(max_p, p)
        return max_p
        
        # sliding window
        # n = len(prices)
        # left = 0 
        # max_p = 0
        # for right in range(n):
        #     while prices[left] > prices[right] and right > left:
        #         left += 1
        #     p = prices[right] - prices[left]
        #     max_p = max(max_p, p)
        # return max_p
