class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []

        for ch in s:
            if ch.isalnum():
                new_s.append(ch.lower())

        if new_s == new_s[::-1]:
            return True
        
        return False

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))