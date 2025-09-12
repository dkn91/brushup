class Solution:
    def validPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        if newStr == newStr[::-1]:
            return True
        tempStr = newStr
        count = 0
        while count < len(tempStr):
            listtempStr = list(tempStr)
            listtempStr[count] = ''
            istempStrpalin = ''.join(listtempStr)
            if istempStrpalin == istempStrpalin[::-1]:
                return True
            count += 1
        return False

obj = Solution()

print(obj.validPalindrome('abca'))
print(obj.validPalindrome('cbbcc'))