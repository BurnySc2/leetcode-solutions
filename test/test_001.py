from python_src.p001_two_sum import Solution


def test_001(benchmark):
    benchmark(Solution().twoSum, [2, 7, 11, 15], 9)
