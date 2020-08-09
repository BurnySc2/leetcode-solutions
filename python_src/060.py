"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List, Any, Generator
from math import factorial


def permutation_generator(my_list: List[Any]) -> Generator[Any, None, None]:
    # Length of list: at least 1
    if len(my_list) == 1:
        yield my_list
        return
    for i, middle in enumerate(my_list):
        remaining_list = my_list[:i] + my_list[i + 1 :]
        for p in permutation_generator(remaining_list):
            yield [middle] + p


def permutation_backwards_generator(my_list: List[Any]) -> Generator[Any, None, None]:
    # Length of list: at least 1
    if len(my_list) == 1:
        yield my_list
        return
    for i in range(len(my_list) - 1, -1, -1):
        middle = my_list[i]
        remaining_list = my_list[:i] + my_list[i + 1 :]
        for p in permutation_backwards_generator(remaining_list):
            yield [middle] + p


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        numbers = list(map(str, range(1, n + 1)))
        amount = factorial(n)

        if amount - k < k:
            permutations = permutation_backwards_generator(numbers)
            for _ in range(amount - k):
                next(permutations)
            return "".join(next(permutations))

        permutations = permutation_generator(numbers)
        for _ in range(k - 1):
            next(permutations)
        return "".join(next(permutations))


# fmt: off
test_cases = [[3, 3], [4, 9], [1, 1], [3, 1], [8, 21092], [9, 233794], [9, 214267]]
results = ["213", "2314", "1", "123", "52378164", "683724591", "635749128"]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.getPermutation(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
