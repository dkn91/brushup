class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' :'(', ']':'[', '}':'{'}
        stack = []

        for ch in s:
            if ch in pairs: #look for closed paran in keys
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack              



print(Solution().isValid('()'))