from typing import List, Tuple
import numpy as np


class Solution:
    @classmethod
    def get_start_end(cls, array_length: int, shift: int) -> Tuple[int, int]:
        start = shift if shift > 0 else 0
        end = array_length if shift >= 0 else array_length + shift
        return start, end

    def shift_and_count(self, a: np.ndarray, b: np.ndarray, x_shift: int, y_shift: int, size: int):
        a_start_y, a_end_y = self.get_start_end(size, y_shift)
        a_start_x, a_end_x = self.get_start_end(size, x_shift)
        b_start_y = size - a_end_y
        b_end_y = size - a_start_y
        b_start_x = size - a_end_x
        b_end_x = size - a_start_x
        a_shifted = a[a_start_y:a_end_y, a_start_x:a_end_x]
        b_shifted = b[b_start_y:b_end_y, b_start_x:b_end_x]
        assert a_shifted.shape == b_shifted.shape, f"{a_shifted.shape} == {b_shifted.shape}"
        return np.count_nonzero((a_shifted & b_shifted) == 1)

    def largestOverlap(self, a: List[List[int]], b: List[List[int]]) -> int:
        size = len(a)
        count = 0
        a_array = np.array(a)
        b_array = np.array(b)
        for x in range(-size + 1, size):
            for y in range(-size + 1, size):
                result = self.shift_and_count(a_array, b_array, x, y, size)
                count = max(count, result)
        return count


if __name__ == "__main__":
    # fmt: off
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    # fmt: on
    length = len(a)
    for y in range(-length + 1, length):
        for x in range(-length + 1, length):
            s1_y, e1_y = Solution.get_start_end(length, y)
            s1_x, e1_x = Solution.get_start_end(length, x)
            s2_y, e2_y = length - e1_y, length - s1_y
            s2_x, e2_x = length - e1_x, length - s1_x
            # s2_y, e2_y = Solution.get_start_end2(length, y)
            # s2_x, e2_x = Solution.get_start_end2(length, x)
            b: np.ndarray = a[s1_y:e1_y, s1_x:e1_x]
            c: np.ndarray = a[s2_y:e2_y, s2_x:e2_x]
            assert b.shape == c.shape, f"{(y, x)} - {b.shape} - {c.shape}"

    # fmt: off
    test_cases = [
        [
            [[1,1,0],
            [0,1,0],
            [0,1,0]],

            [[0,0,0],
            [0,1,1],
            [0,0,1]]
        ],
    ]
    results = [
        3
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.largestOverlap(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
