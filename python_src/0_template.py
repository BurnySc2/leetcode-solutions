"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


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


# fmt: off
test_cases = [5]
results = [[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.generate(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
