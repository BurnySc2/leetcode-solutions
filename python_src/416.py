from typing import List


class Solution:
    def rebuild_sum(self, lookup: List[int], target: int):
        assert lookup[target] > -1
        my_summands = []
        while target != 0:
            my_summands.append(lookup[target])
            target -= lookup[target]
        return my_summands

    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        target = nums_sum // 2
        my_lookup = [-1 for _ in range(target + 1)]
        my_lookup[0] = 0
        for num in nums:
            for i in range(target, -1, -1):
                if my_lookup[i] > -1:
                    new_index = num + i
                    if new_index > target:
                        continue
                    if new_index < 0:
                        break
                    if my_lookup[new_index] == -1:
                        my_lookup[new_index] = num
                        if new_index == target:
                            # Reconstruct how the sum is set together
                            # summands = self.rebuild_sum(my_lookup, target)
                            # sorted_nums = sorted(nums, reverse=True)
                            # sorted_summands = sorted(summands, reverse=True)
                            # print(f"Sorted nums: {sorted_nums}")
                            # print(f"Target: {target}")
                            # print(f"Sorted summands: {sorted_summands}")
                            # print()
                            return True
        return False

        # if result:
        #     print(f"Result for {nums} is:")
        #     print(f"{result}")
        #     assert sum(result) == nums_sum // 2
        #     return True
        # return False


#
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         nums_sum = sum(nums)
#         if nums_sum % 2 == 1:
#             return False
#         nums.sort(reverse=True)
#         result = self.can_partition_recursive(tuple(nums), nums_sum // 2)
#         if result:
#             print(f"Result for {nums} is:")
#             print(f"{result}")
#             assert sum(result) == nums_sum // 2
#             return True
#         return False
#
#     @lru_cache(maxsize=None)
#     def can_partition_recursive(self, nums: tuple, target: int) -> List[int]:
#         if not nums:
#             return []
#         min_value = min(nums)
#         if min_value > target:
#             return []
#         temp_sum = sum(nums)
#         if temp_sum < target:
#             return []
#
#         for index, i in enumerate(nums):
#             if i > target:
#                 continue
#             if i == target:
#                 return [i]
#             if i < target:
#                 result = self.can_partition_recursive(nums[index + 1:], target - i)
#                 if result:
#                     return [i] + result
#         return []

# fmt: off
test_cases = [
    # [
    #     71, 70, 66, 54, 32, 63, 38, 98, 4, 22, 61, 40, 6, 8, 6, 21, 71, 36, 30, 34, 44, 60, 89, 53, 60, 56, 73, 14, 63,
    #     37, 15, 58, 51, 88, 88, 32, 80, 32, 10, 89, 67, 29, 68, 65, 34, 15, 88, 8, 57, 78, 37, 63, 73, 65, 47, 39, 32,
    #     74, 31, 44, 43, 4, 10, 8, 96, 22, 58, 87, 29, 99, 79, 13, 96, 21, 62, 71, 34, 55, 72, 3, 96, 7, 36, 64, 30, 6,
    #     14, 87, 12, 90, 40, 13, 29, 21, 94, 33, 99, 86, 4, 100
    # ],
    # [
    #     4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16,
    #     20, 20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32,
    #     32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44,
    #     48, 48, 48, 48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60,
    #     60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72,
    #     76, 76, 76, 76, 76, 76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88,
    #     88, 88, 88, 88, 92, 92, 92, 92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99
    # ],
    [
        71, 70, 66, 54, 32, 63, 38, 98, 4, 22, 61, 40, 6, 8, 6, 21, 71, 36, 30, 34, 44, 60, 89, 53, 60, 56, 73, 14, 63,
        37, 15, 58, 51, 88, 88, 32, 80, 32, 10, 89, 67, 29, 68, 65, 34, 15, 88, 8, 57, 78, 37, 63, 73, 65, 47, 39, 32,
        74, 31, 44, 43, 4, 10, 8, 96, 22, 58, 87, 29, 99, 79, 13, 96, 21, 62, 71, 34, 55, 72, 3, 96, 7, 36, 64, 30, 6,
        14, 87, 12, 90, 40, 13, 29, 21, 94, 33, 99, 86, 4, 100
    ],
    [23, 13, 11, 7, 6, 5, 5],
    [100],
    [1, 2, 3, 4, 5, 6, 7],
    [2, 2, 3, 5],
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [1, 3, 5, 7, 9, 11],
    [
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
        99, 97
    ],
]

results = [
    # True,
    # False,
    True,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.canPartition(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
