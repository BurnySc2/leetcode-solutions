"""
Teemo Attacking

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
"""
from typing import List
import math

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Never poisoned
        if not timeSeries:
            return 0

        start_time = -math.inf
        end_time = -math.inf
        total_duration = 0
        for time_stamp in timeSeries:
            if end_time < time_stamp:
                # Add previous poison duration
                if end_time != -math.inf:
                    total_duration += end_time - start_time
                # Set current poison duation
                start_time = time_stamp
                end_time = start_time + duration
            else:
                # Poison was reapplied before end was reached
                end_time = time_stamp + duration

        return total_duration + end_time - start_time


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[1, 2], 2],
        [[1, 4], 2],
    ]
    results = [
        3,
        4,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.findPoisonedDuration(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
