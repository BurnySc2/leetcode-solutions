"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        valid = []
        for i, h1 in enumerate(A):
            for j, h2 in enumerate(A):
                if i == j:
                    continue
                if 0 <= h1 * 10 + h2 < 24:
                    for k, m1 in enumerate(A):
                        for l, m2 in enumerate(A):
                            if k == l or k in {i, j} or l in {i, j}:
                                continue
                            if 0 <= m1 * 10 + m2 < 60:
                                valid.append(f"{h1}{h2}:{m1}{m2}")
        return max(valid, default="")


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [1, 2, 3, 4],
        [1, 9, 3, 4],
        [1, 9, 2, 4],
        [9, 9, 1, 2],
        [5, 5, 5, 5],
    ]
    results = [
        "23:41",
        "19:43",
        "21:49",
        "19:29",
        "",
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.largestTimeFromDigits(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
