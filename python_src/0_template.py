"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode") -> bool:
        if not isinstance(other, ListNode):
            return False

        if self.length(self) != self.length(other):
            return False

        first, second = self, other
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        return True

    def __repr__(self) -> str:
        seen = set()
        nodes = []
        current = self
        while 1:
            if id(current) in seen:
                return "REPEATED NODES " + " -> ".join(map(str, nodes))
            seen.add(id(current))
            nodes.append(current.val)
            if not current.next:
                return " -> ".join(map(str, nodes))
            current = current.next

    @classmethod
    def length(cls, node: "ListNode") -> int:
        l = 0
        start = node
        while start:
            start = start.next
            l += 1
        return l

    @classmethod
    def from_list(cls, my_list: List[int]) -> "ListNode":
        assert my_list
        start = cls(my_list[0])
        cur = start
        for i in my_list[1:]:
            cur.next = cls(i)
            cur = cur.next
        return start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal = [[1]]
        for row_index in range(1, numRows):
            new_row = []
            new_row.append(1)
            for column_index in range(row_index - 1):
                value = pascal[row_index - 1][column_index] + pascal[row_index - 1][column_index + 1]
                new_row.append(value)
            new_row.append(1)
            pascal.append(new_row)
        return pascal


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        5
    ]
    results = [
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.generate(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
