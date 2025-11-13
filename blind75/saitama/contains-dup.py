from typing import List

class Solution:
    def containsDups(self, nums: List[int], k: int)-> bool:
        for i in range(len(nums)):
            #print(i)
            for j in range(i+1, len(nums)):
                print(j)
                if nums[i] == nums[j]:
                    print(i,j)
                    if abs(i-j) <= k:
                        return True 
        return False

print(Solution().containsDups(nums = [1,2,3,1], k = 3))
print(Solution().containsDups(nums = [1,2,3,1,2,3], k = 2))

'''
Example 1:


Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
i = 2, j = 3
i-j<=3


Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 '''