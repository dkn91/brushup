class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Peak must be on the left (including mid)
                right = mid
            else:
                # Peak must be on the right
                left = mid + 1
        
        return left  # left == right -> peak index

obj = Solution()
print(obj.findPeakElement(nums = [1,2,3,1]))