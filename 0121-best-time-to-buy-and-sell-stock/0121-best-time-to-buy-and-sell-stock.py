class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        mini = prices[0]
        current_profit = 0
        for i in range(len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            print(mini)
            current_profit =  prices[i] - mini
            # print(current_profit)
            max_profit = max(current_profit,max_profit)
        return max_profit