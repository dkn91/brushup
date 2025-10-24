from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )

node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(15)
node.left.left = TreeNode(3)
node.left.right = TreeNode(7)
node.right.right = TreeNode(18)
print(Solution().rangeSumBST(node, 7, 15))