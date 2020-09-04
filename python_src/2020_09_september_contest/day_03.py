class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for right in range(1, len(s) // 2 + 1):
            if len(s) % right != 0:
                continue
            word = s[0:right]
            times = len(s) // len(word)
            if word * times == s:
                return True
        return False


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        "bb",
        "ababba",
        "abab",
        "aba",
        "abcabcabcabc",
        "abac",
    ]
    results = [
        True,
        False,
        True,
        False,
        True,
        False,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.repeatedSubstringPattern(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
