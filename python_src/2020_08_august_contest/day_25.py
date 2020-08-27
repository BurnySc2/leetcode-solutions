from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[float]):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache()
        def dp(i: int):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [[1,4,6,7,8,20],[2,7,15]],
        [[1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]],
    ]
    results = [
        11,
        17,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy()
        my_result = app.mincostTickets(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
