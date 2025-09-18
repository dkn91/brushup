# This assumes you are given a list of NestedInteger objects
# Each NestedInteger has:
# - isInteger() -> bool
# - getInteger() -> int
# - getList() -> [NestedInteger]
class NestedInteger:
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = [NestedInteger(v) for v in value]

    def isInteger(self):
        return self._integer is not None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

# Example local test:
nestedList = [NestedInteger([1, 1]), NestedInteger(2), NestedInteger([1, 1])]

class Solution:
    def depthSum(self, nestedList):
        def dfs(nestedList, depth):
            total = 0
            for ni in nestedList:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        
        return dfs(nestedList, 1)

obj = Solution()
print(obj.depthSum(nestedList))