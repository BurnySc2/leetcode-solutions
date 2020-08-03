"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        return False


test_cases = [121, -121, 10]
results = [True, False, False]

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        assert (
            app.isPalindrome(test_case) == correct_result
        ), f"My result: {app.isPalindrome(test_case)}, correct result: {correct_result}"
