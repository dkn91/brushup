from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        current = 1
        i = 0

        while True:
            if i < len(arr) and arr[i] == current:
                i += 1  # number exists in array
            else:
                missing += 1  # number is missing
                if missing == k:
                    return current
            current += 1
    
print(Solution().findKthPositive([1,2,3,4], 2))