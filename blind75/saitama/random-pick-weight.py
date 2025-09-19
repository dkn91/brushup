from typing import List

import random
import bisect

class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        prefix = 0
        
        for weight in w:
            prefix += weight
            self.prefix_sums.append(prefix)
        
        self.total_sum = prefix

    def pickIndex(self):
        # Pick random number in [1, total_sum]
        target = random.randint(1, self.total_sum)
        
        # Binary search for first prefix >= target
        idx = bisect.bisect_left(self.prefix_sums, target)
        return idx

# Your Solution object will be instantiated and called as such:
w = [1, 3]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)