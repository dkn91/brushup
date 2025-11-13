from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1  # pretend a number just before lower

        # Go through all numbers + one beyond upper for boundary
        for i in range(len(nums) + 1):
            # current = next number if exists, else upper + 1 (after range)
            curr = nums[i] if i < len(nums) else upper + 1

            # If there's a gap between prev and curr
            if curr - prev >= 2:
                result.append(self.formatRange(prev + 1, curr - 1))

            prev = curr  # move window

        return result

    def formatRange(self, start, end):
        return str(start) if start == end else f"{start}->{end}"

print(Solution().findMissingRanges(nums = [0, 1, 3, 50, 75, 81], lower = 0, upper = 99))