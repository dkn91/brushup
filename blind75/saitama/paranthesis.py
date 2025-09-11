class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openparanthesisPresent = False
        open_count = 0
        new_s = []
        for v in s:
            if v == ')' and open_count == 0:
                continue
            if v == '(':
                open_count += 1
            elif v == ')':
                open_count -= 1
            
            new_s.append(v)

            #reversed
        close_count = 0
        result = []
        for v in reversed(new_s): 
            if v == '(' and close_count == 0:
                continue
            if v == ')':
                close_count += 1
            elif v == '(':
                close_count -= 1
            
            result.append(v)

        return ''.join(reversed(result))
obj = Solution()
print(obj.minRemoveToMakeValid("))a(("))
print(obj.minRemoveToMakeValid("a)b(c)d"))
print(obj.minRemoveToMakeValid("lee(t(c)o)de)"))