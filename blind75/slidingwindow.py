from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
    
obj = Solution()
print(obj.maxProfit([10,1,5,6,7,1]))  # 6
print(obj.maxProfit([7, 6, 4, 3, 1]))  # 0
print(obj.maxProfit([1, 2, 3, 4, 5]))  # 4
print(obj.maxProfit([2, 4, 1]))  # 0