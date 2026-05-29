class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
                continue
            
            max_profit = max(price - lowest_price, max_profit)

        return max_profit