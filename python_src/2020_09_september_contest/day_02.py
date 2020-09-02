"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i + 1 :], start=i + 1):
                if j - i > k:
                    break
                if abs(val2 - val1) > t:
                    continue
                return True

        return False

        # Alternative but slow solution:

        # sorted_nums = sorted(nums)
        #
        # valid = set()
        # for i, val1 in enumerate(sorted_nums):
        #     for val2 in sorted_nums[i + 1 :]:
        #         if val2 - val1 > t:
        #             break
        #         valid.add((val2, val1))
        # if not valid:
        #     return False
        #
        # for i, val1 in enumerate(nums):
        #     for j, val2 in enumerate(nums[i + 1 :], start=i + 1):
        #         if j - i > k:
        #             break
        #         if (val2, val1) in valid or (val1, val2) in valid:
        #             return True
        # return False


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[2, 1], 1, 1],
        [[1, 2, 3, 1], 3, 0],
        [[1, 0, 1, 1], 1, 2],
        [[1, 5, 9, 1, 5, 9], 2, 3],
    ]
    results = [
        True,
        True,
        False,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.containsNearbyAlmostDuplicate(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
