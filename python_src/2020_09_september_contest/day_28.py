"""
Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

https://leetcode.com/problems/subarray-product-less-than-k/
"""
from typing import List

""" Wrong solution, my brain doesn't work """
class Solution:
    def __init__(self):
        self.count = 0

    def add_products(self, nums: List[int], k: float, product: int):
        """
        nums = [10, 5, 2, 6]
        10 < 100
        10 * 5 < 100
        not: 10 * 5 * 2 < 100 => return
        5 < 100
        5 * 2 < 100
        5 * 2 * 6 < 100
        end of list
        2 < 100
        2 * 6 < 100
        end of list
        6 < 100
        end of list
        """
        for index, factor in enumerate(nums):
            if product * factor < k:
                self.count += 1
                remaining_list = nums[index + 1:]
                if remaining_list:
                    self.add_products(remaining_list, k, product * factor)
            elif product != 1:
                return

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        self.count = 0
        self.add_products(nums, k, 1)
        return self.count


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[10, 5, 2, 6], 100],
    ]
    results = [
        8,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.numSubarrayProductLessThanK(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
