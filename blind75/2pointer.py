from typing import List

class Solution:
    def isPalindrome2(self, s: str) -> bool:
        s2 = []
        for c in s:
            if c.isalnum():
                s2.append(c.lower())
        s = ''.join(s2)
        left, right = 0, len(s) - 1
        print(s)
        while left < right:
            if (s[left].lower() != s[right].lower()):
                print(s[left], s[right], left, right)
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        print(newStr, newStr[::-1])
        return newStr == newStr[::-1]

obj = Solution()
print(obj.isPalindrome("Was it a car or a cat I saw?"))  # True