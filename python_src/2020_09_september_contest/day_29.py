"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

https://leetcode.com/problems/word-break/
"""
from functools import lru_cache

class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def dfs(k):
            if k == n: return True
            for i in range(k + 1, n + 1):
                if s[k:i] in wordSet and dfs(i):
                    return True
            return False

        return dfs(0)
if __name__ == "__main__":
    # fmt: off
    test_cases = [
        ["leetcode", ["leet", "code"]],
        ["applepenapple", ["apple", "pen"]],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
        ["aaaaaaaaaab", ["aaaa", "aaa"]],
    ]
    results = [
        True,
        True,
        False,
        False
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.wordBreak(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
