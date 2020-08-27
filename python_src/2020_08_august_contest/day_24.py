# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_left_leaves(self, root: TreeNode, was_left=False) -> int:
        left = self.get_left_leaves(root.left, True) if root.left else 0
        right = self.get_left_leaves(root.right) if root.right else 0
        value = root.val if was_left and not root.left and not root.right else 0
        return left + right + value

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_left_leaves(root)


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    ]
    results = [
        4
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case
        my_result = app.sumOfLeftLeaves(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
