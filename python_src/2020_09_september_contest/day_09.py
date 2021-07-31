from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        for s1, s2 in zip_longest(v1, v2, fillvalue=0):
            i1, i2 = int(s1), int(s2)
            if i1 < i2:
                return -1
            elif i1 > i2:
                return 1
        return 0


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        ["0.1", "1.1"],
        ["1.0.1", "1"],
        ["7.5.2.4", "7.5.3"],
        ["1.01", "1.001"],
        ["1.0", "1.0.0"],
    ]
    results = [
        -1,
        1,
        -1,
        0,
        0,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.compareVersion(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
