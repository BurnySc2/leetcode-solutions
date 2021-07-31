"""
Evaluate Division

You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from typing import List, Dict
from fractions import Fraction

# TODO Not yet solved
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        values: Dict[str, Fraction] = {}
        for (a, b), value in zip(equations, values):
            if a not in values:
                pass



        pass



if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]]
    ]
    results = [
        [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.calcEquation(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
