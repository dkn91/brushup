# This assumes you are given a list of NestedInteger objects
# Each NestedInteger has:
# - isInteger() -> bool
# - getInteger() -> int
# - getList() -> [NestedInteger]


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
print(obj.depthSum([[1,1],2,[1,1]]))