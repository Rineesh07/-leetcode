class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        ans = prices
        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                ans[idx] = prices[idx] - prices[i]
            stack.append(i)
        for i in range(n):
            if ans[i]  == 0:
                ans[i] = prices[i]
        return ans