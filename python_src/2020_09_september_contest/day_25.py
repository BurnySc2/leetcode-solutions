"""
Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        compare = lambda a, b: -1 if a + b > b + a else 1 if a + b < b + a else 0
        return str(int("".join(sorted(map(str, nums), key=cmp_to_key(compare)))))


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [432, 43243],
        [34323, 3432],
        [9, 91, 92, 921, 8],
        [111311, 1113],
        [10, 2],
        [3, 30, 34, 5, 9],
        [1],
        [10],
    ]
    results = [
        "43243432",
        "343234323",
        "992921918",
        "1113111311",
        "210",
        "9534330",
        "1",
        "10",
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.largestNumber(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
