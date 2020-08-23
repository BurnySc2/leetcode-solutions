"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List

# Problem 1 https://leetcode.com/problems/most-visited-sector-in-a-circular-track
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        r = []
        i = rounds[0]
        while i != rounds[-1]:
            r.append(i)
            i += 1
            if i > n:
                i -= n
        r.append(i)
        r.sort()
        return r


# Problem 2 https://leetcode.com/problems/maximum-number-of-coins-you-can-get
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(i for i in sorted(piles, reverse=True)[1 : 2 * len(piles) // 3 : 2])


if __name__ == "__main__":
    r = Solution().maxCoins([2, 4, 1, 2, 7, 8])
    print(r)
    assert r == 9

    r = Solution().maxCoins([4, 4, 17, 7, 16, 16, 16, 15, 2, 3, 1, 17, 6, 12, 9])
    print(r)
    assert r == 63

# Problem 3 https://leetcode.com/problems/find-latest-group-of-size-m
import re


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ones = "1" * m
        pattern = f"^({ones}0)|(0{ones})$|(0{ones}0)|^({ones})$"
        p = re.compile(pattern)
        array = ["1"] * len(arr)
        last = -1
        for count, i in enumerate(arr[::-1]):
            if p.search("".join(array)):
                last = len(arr) - count
                break
            array[i - 1] = "0"
        return last


if __name__ == "__main__":
    pattern = "^(1110)|(0111)$|(01110)|^(111)$"
    p = re.compile(pattern)

    assert re.search(p, "111")
    assert re.search(p, "0111")
    assert re.search(p, "1110")
    assert re.search(p, "01110")
    assert not re.search(p, "011110")
    assert not re.search(p, "11110")
    assert not re.search(p, "01111")
    a = re.search(p, "01111")

    pattern = "^(10)|(01)$|(010)|^(1)$"
    p = re.compile(pattern)
    s = p.search("11101")
    assert re.search(p, "11101")

    r = Solution().findLatestStep([3, 5, 1, 2, 4], 1)
    assert r == 4, f"{r}"
