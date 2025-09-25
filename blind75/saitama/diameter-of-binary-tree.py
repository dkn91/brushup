class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Diameter passing through this node
            self.diameter = max(self.diameter, left + right)
            
            # Return depth
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter
