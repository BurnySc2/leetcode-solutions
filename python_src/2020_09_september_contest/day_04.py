from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return [0]

        right = {}
        for index, char in enumerate(S):
            right[char] = index

        return_lists = []
        char = S[0]
        l = 0
        r = right[char]
        for index, char in enumerate(S):
            if index > r:
                return_lists.append(r - l + 1)
                l = index
            if right[char] > r:
                r = right[char]
        return_lists.append(r - l + 1)

        return return_lists


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        "aba",
        "abcd",
        "",
        "ababcbacadefegdehijhklij"
    ]
    results = [
        [3],
        [1, 1, 1, 1],
        [0],
        [9, 7, 8]
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.partitionLabels(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
