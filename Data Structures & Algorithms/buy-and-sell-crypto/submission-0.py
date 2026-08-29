class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window

        # Brute Force
        results_list = [0]
        length = len(prices)
        for i in range(length):
            for j in range(i+1, length):
                profit = prices[j] - prices[i]
                results_list.append(profit)
        return max(results_list)

