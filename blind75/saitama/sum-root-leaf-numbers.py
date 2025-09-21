class Solution:
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            current = current * 10 + node.val
            
            # If it's a leaf, return the number formed
            if not node.left and not node.right:
                return current
            
            # Otherwise, sum results from children
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)
