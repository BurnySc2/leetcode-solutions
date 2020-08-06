import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        power = int(math.log(num, 4))
        original = 4 ** power
        return original == num
