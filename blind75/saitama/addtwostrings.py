class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res = []
        carry = 0

        while i >= 0 and j >= 0 or carry:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            res.append(str(total%10))

            i -= 1
            j -= 1

        return (''.join(res[::-1]))
    
print(Solution().addStrings(num1 = "456", num2 = "77"))
