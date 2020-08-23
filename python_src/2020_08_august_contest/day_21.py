from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 == 1]


# fmt: off
test_cases = [
    [3,1,2,4],
]
results = [
    [2,4,3,1],
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy()
        my_result = app.sortArrayByParity(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
