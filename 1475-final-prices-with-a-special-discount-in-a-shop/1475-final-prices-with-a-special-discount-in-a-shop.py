class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discount = []
        for i in range(n):
            d = 0 
            for j in range(i+1 , n):
                if prices[j] <= prices[i]:
                    d = prices[j]
                    break
            discount.append(d)
        print(discount)
        pay = [0] * n
        for i in range(n):
            pay[i] = prices[i] - discount[i]
        return pay