from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [num*num for num in nums]
        new_nums.sort()
        return new_nums

print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))