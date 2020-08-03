"""
Given a collection of distinct integers, return all possible permutations.

https://leetcode.com/problems/permutations/
"""


from typing import Set, Tuple, List, Generator
from collections import Counter
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions: List[int] = []
        for permutation in itertools.permutations(nums):
            solutions.append(list(permutation))
        return solutions


test_cases = [[1, 2, 3]]
results = [[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]]

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_solution = app.permute(test_case)
        assert my_solution == correct_result, f"My result: {my_solution}, correct result: {correct_result}"
