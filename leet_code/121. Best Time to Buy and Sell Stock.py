class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for i, price in enumerate(prices):
            if min_price > price:
                min_price = price
            
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            
        return max_profit