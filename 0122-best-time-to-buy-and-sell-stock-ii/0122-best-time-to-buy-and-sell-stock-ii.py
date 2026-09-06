class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        profit = 0 
        i = 0
        n = len(prices)
        while i < n - 1:
            j = i + 1
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                print(profit)
                max_profit += profit
            i += 1
        return max_profit