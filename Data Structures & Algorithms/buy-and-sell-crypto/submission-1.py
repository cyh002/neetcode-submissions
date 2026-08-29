class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window

        # Brute Force
        # results_list = [0]
        # length = len(prices)
        # for i in range(length):
        #     for j in range(i+1, length):
        #         profit = prices[j] - prices[i]
        #         results_list.append(profit)
        # return max(results_list)

        # Sliding Window
        length = len(prices)
        L = 0 
        max_profit = 0
        for R in range(length):
            if prices[L] > prices[R]:
                # window is invalid if prices drops
                L = R
            else:
                # window is valid
                current_profit = prices[R] - prices[L]
                max_profit = max(current_profit, max_profit)
        return max_profit

