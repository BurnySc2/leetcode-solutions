# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random
from collections import Counter


def rand7():
    return random.randint(1, 7)


####################################################


class Solution:
    def __init__(self):
        self.amount = 4
        self.upper_limit = int("6" * self.amount, 7)
        self.divisor = self.upper_limit // 10

    def rand10(self):
        n = int("".join(f"{rand7() - 1}" for _ in range(self.amount)), 7)

        rand_number = n // self.divisor
        if rand_number == 0:
            rand_number = 10
        return rand_number

    def rand_team(self):
        return round(rand7() * 10 / 7)


####################################################

if __name__ == "__main__":
    c = Counter()
    s = Solution()
    for i in range(10000):
        # c[s.rand10()] += 1
        c[s.rand_team()] += 1
    print(c)
