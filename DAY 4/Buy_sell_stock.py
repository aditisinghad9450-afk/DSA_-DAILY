class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        min_price=prices[0]
        max_price=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
                if (prices[i]- min_price)>profit:
                    profit+=1

        return profit
