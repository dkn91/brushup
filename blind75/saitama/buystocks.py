from typing import List
class Solution:
    def maxProfits(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
            
        return max_profit
    
print(Solution().maxProfits([7,1,5,3,6,4]))
print(Solution().maxProfits([7,6,4,3,1]))