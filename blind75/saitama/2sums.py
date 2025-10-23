from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two loops [3,2,4]
        for i in range(len(nums)-1):
            print(i)
            for k in range(i+1, len(nums)):
                print(k)
                if (nums[i] + nums[k]) == target:
                    return [i, k]

obj = Solution()
nums = [3,2,4]
print(obj.twoSum(nums, target=6))
