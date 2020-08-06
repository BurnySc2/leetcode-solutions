# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s: str = "".join(c.lower() for c in s if c.isalnum())
        if not s:
            return True
        return s == s[::-1]


if __name__ == "__main__":
    a = Solution()
    s = a.isPalindrome("A man, a plan, a canal: Panama")

    print(s)
