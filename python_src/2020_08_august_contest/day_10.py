from typing import List, Tuple


class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(number) - 64) * 26 ** index for index, number in enumerate(s[::-1]))


# fmt: off
test_cases = [
    "A",
    "AB",
    "ZY",
]
results = [
    1,
    28,
    701,
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.titleToNumber(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
