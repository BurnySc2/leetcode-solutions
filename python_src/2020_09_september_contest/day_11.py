from typing import List
from functools import lru_cache


class Solution:
    def __init__(self):
        self.nums = []

    @lru_cache()
    def product(self, start_index: int, end_index: int):
        if start_index == end_index:
            return self.nums[start_index]
        return self.nums[end_index] * self.product(start_index, end_index - 1)

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        to_add = set()

        # Remove 1s
        if 1 in nums:
            to_add.add(1)
        nums = [i for i in nums if i != 1]

        # Remove pair of -1's
        i = 2
        while i < len(nums):
            val1 = nums[i - 2]
            if val1 == -1:
                i += 1
                continue
            val2 = nums[i - 1]
            val3 = nums[i]
            if val2 == val3 == -1:
                del nums[i - 1]
                del nums[i - 1]
                to_add.add(-1)
                to_add.add(1)
                to_add.add(-val1)
            else:
                i += 1

        self.nums = nums
        self.product.cache_clear()

        products = set()
        for start_index in range(len(nums)):
            if nums[start_index] == 0:
                to_add.add(0)
                continue
            for end_index in range(start_index, len(nums)):
                if nums[end_index] == 0:
                    to_add.add(0)
                    break
                result = self.product(start_index, end_index)
                products.add(result)
        return max(products | to_add)


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [-3, -1, -1],
        [-1, -1],
        [-1, -1, 1],
        [0, 1],
        [0, 2],
        [0],
        [0, 0],
        [1,0,-1,2,3,-5,-2],
        [2,3,-2,4],
        [-2,0,-1],
    ]
    results = [
        3,
        1,
        1,
        1,
        2,
        0,
        0,
        60,
        6,
        0,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.maxProduct(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
