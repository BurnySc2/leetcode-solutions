from typing import List, Tuple
import math

# TOO SLOW, works in rust, problem 123 'p123.rs'
class Solution:
    def find_indices(self, my_list: List[int]) -> Tuple[List[int], List[int]]:
        """ This functions returns a tuple of:
        For a given list of [1, 5, 4, 6] this will return the indices of 1 and 4, so [0, 2]
        For a given list of [1, 5, 4, 6] this will return the indices of 5 and 6, so [1, 3]
        """
        lowest = math.inf
        lowest_index = None
        largest = -math.inf
        largest_index = None
        mins = []
        maxs = []
        for i, value in enumerate(my_list):
            if value < lowest:
                lowest_index, lowest = i, value
            elif value > lowest:
                if lowest_index is not None:
                    mins.append(lowest_index)
                    lowest_index = None
                lowest = value

            # If mins has at least one item
            if mins:
                if value > largest:
                    largest_index, largest = i, value
                elif value < largest:
                    if largest_index is not None:
                        maxs.append(largest_index)
                        largest_index = None
                    largest = value

        if lowest_index is not None:
            mins.append(lowest_index)
        if largest_index is not None:
            maxs.append(largest_index)
        return mins, maxs

    def find_profit(self, prices: List[int], mins: List[int], maxs: List[int]) -> int:
        largest_profit = 0
        # Try to find N shape profit
        for min1_index, min1 in enumerate(mins):
            min1_val = prices[min1]
            for max1_index, max1 in enumerate(maxs):
                max1_val = prices[max1]
                if max1_val <= min1_val or max1 <= min1:
                    continue
                profit1 = max1_val - min1_val
                # Try to find '/' shape profit
                if profit1 > largest_profit:
                    largest_profit = profit1
                for min2 in mins[min1_index + 1 :]:
                    if min2 <= max1:
                        continue
                    min2_val = prices[min2]
                    for max2 in maxs[max1_index + 1 :]:
                        if max2 <= min2:
                            continue
                        max2_val = prices[max2]
                        profit2 = max2_val - min2_val
                        if profit1 + profit2 > largest_profit:
                            largest_profit = profit1 + profit2
        return largest_profit

    def maxProfit(self, prices: List[int]) -> int:
        mins, maxs = self.find_indices(prices)
        return self.find_profit(prices, mins, maxs)


# fmt: off
test_cases = [
    [3, 3, 5, 0, 0, 3, 1, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1],
    [1, 5, 4, 6],
    [20, 15, 19, 14, 18, 10, 14, 5, 8, 6, 10, 3],
]
results = [
    6,
    4,
    0,
    6,
    9,
]
# fmt: on


assert Solution().find_indices([1, 5, 4, 6]) == ([0, 2], [1, 3]), f"{Solution().find_indices([1, 5, 4, 6])}"
assert Solution().find_indices([1, 2, 3, 4, 5]) == ([0], [4]), f"{Solution().find_indices([1, 2, 3, 4, 5])}"
assert Solution().maxProfit([1, 5, 4, 6]) == 6, f"{Solution().maxProfit([1, 5, 4, 6])}"

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy()
        my_result = app.maxProfit(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
