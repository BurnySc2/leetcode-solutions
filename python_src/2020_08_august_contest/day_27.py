from typing import List, Dict, Tuple
import math


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []

        intervals = [[tuple(interval), i] for i, interval in enumerate(intervals)]
        intervals_sorted = sorted(intervals, key=lambda i: (i[0][0], i[1]))

        results: Dict[Tuple[int, int], int] = {}
        last_index = 0
        last_interval_end = math.inf
        for i, (interval1, index1) in enumerate(intervals_sorted):
            if interval1 in results:
                continue
            if interval1[1] < last_interval_end:
                last_index = 0
            last_interval_end = interval1[1]
            start_index = max(last_index, i + 1)
            j = i
            for j, (interval2, index2) in enumerate(intervals_sorted[start_index:], start=start_index):
                if interval1[1] <= interval2[0]:
                    results[interval1] = index2
                    break
            last_index = j

        return_result = []
        for interval, i in intervals:
            return_result.append(results.get(interval, -1))
        return return_result


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[1, 2]],
        [[3,4], [2,3], [1,2]],
        [[1,4], [2,3], [3,4]],
        [[1, 2], [2, 3], [2, 3], [3, 4]],
    ]
    results = [
        [-1],
        [-1, 0, 1],
        [-1, 2, -1],
        [1,3,3,-1],
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.findRightInterval(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
