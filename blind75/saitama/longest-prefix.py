from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # start with the first word
        
        for word in strs[1:]:
            # shorten prefix until it matches the start of 'word'
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                print(prefix)
                if not prefix:
                    return ""
        
        return prefix

print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))