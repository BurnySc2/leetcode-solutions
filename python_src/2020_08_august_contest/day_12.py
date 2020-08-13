from typing import List

from math import factorial


class Solution:
    @staticmethod
    def ncr(n: int, k: int):
        return factorial(n) // (factorial(n - k) * factorial(k))

    def getRow(self, rowIndex: int) -> List[int]:
        return [self.ncr(rowIndex, k) for k in range(rowIndex + 1)]


# fmt: off
test_cases = [
    3,
    0,
    1,
    2,
]
results = [
    [1, 3, 3, 1],
    [1],
    [1, 1],
    [1, 2, 1],
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.getRow(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
