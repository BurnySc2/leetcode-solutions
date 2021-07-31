class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode, number: int = 0) -> int:
        number = (number << 1) + root.val
        if not (root.left or root.right):
            return number
        left_sum = self.sumRootToLeaf(root.left, number) if root.left else 0
        right_sum = self.sumRootToLeaf(root.right, number) if root.right else 0
        return left_sum + right_sum
