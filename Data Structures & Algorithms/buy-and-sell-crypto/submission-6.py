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
