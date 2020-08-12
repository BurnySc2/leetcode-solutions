from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        last_value = count = 0
        for value in sorted(citations, reverse=True):
            if value < count:
                return min(count, last_value)
            count, last_value = count + 1, value
        return min(count, last_value)


# import math
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         my_dict = {}
#         for i in citations:
#             if i in my_dict:
#                 my_dict[i] += 1
#             else:
#                 my_dict[i] = 1
#         min_key = math.inf
#         amount = 0
#         for key in sorted(my_dict.keys(), reverse=True):
#             if amount >= key:
#                 return min(amount, min_key)
#             amount += my_dict[key]
#             min_key = key
#         return min(amount, min_key)


""" Best solution:
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        citations.sort(reverse=True)
        h = [0]
        for idx, val in enumerate(citations, start=1):
            if val >= idx:
                h.append(idx)
        return max(h)
"""

# fmt: off
test_cases = [
    [3, 0, 6, 1, 5],
    [3, 0, 6, 1, 5, 4, 7],
    [],
    [1, 2, 2],
    [1, 1],
    [2],
    [1, 2, 2, 2],
]
results = [
    3,
    4,
    0,
    2,
    1,
    1,
    2,
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.hIndex(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
