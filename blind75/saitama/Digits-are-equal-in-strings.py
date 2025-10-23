from typing import cast

class Solution:
    def DigitsAreEqual(self, s: str) -> bool:
        #convert list of int a = [3,9,0,2]
        s2 = [int(a) for a in s]
        new_s = []
        #loop till only 2 element left
        while len(s2) > 2:
            new_s = [(s2[i] + s2[i+1]) % 10 for i in range(0,len(s2)-1)]
            s2 = new_s

        if s2[0] == s2[1]:
            return True
        return False


obj = Solution()
s= "3902"
print(obj.DigitsAreEqual(s))
