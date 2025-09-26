# LeetCode's TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # node value
        self.left = left      # left child (TreeNode or None)
        self.right = right    # right child (TreeNode or None)

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
