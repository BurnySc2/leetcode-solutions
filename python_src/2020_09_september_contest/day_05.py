from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def in_order_traversal(self, root: TreeNode, nodes: List[int] = None):
        if not root:
            return
        if nodes is None:
            nodes = []
        if root.left:
            self.in_order_traversal(root.left, nodes)
        nodes.append(root.val)
        if root.right:
            self.in_order_traversal(root.right, nodes)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        i = j = 0
        list1 = []
        list2 = []
        self.in_order_traversal(root1, list1)
        self.in_order_traversal(root2, list2)
        merged = []
        while i < len(list1) or j < len(list2):
            value1 = list1[i] if i < len(list1) else None
            value2 = list2[j] if j < len(list2) else None
            if value2 is None:
                i += 1
                merged.append(value1)
            elif value1 is None:
                j += 1
                merged.append(value2)
            elif value1 < value2:
                i += 1
                merged.append(value1)
            else:
                j += 1
                merged.append(value2)
        return merged
