from dataclasses import dataclass
import math


@dataclass
class Formula:
    m: int
    n: int

    def __str__(self):
        return f"g({self.m}, {self.n}) = {self.m} ^ {self.n} + {self.m} | {self.n} + {self.m} & {self.n} == {self.compute()}"
        # return f"g({self.m}, {self.n}) = {self.m} ^ {self.n} == {self.compute()}"
        # return f"g({self.m}, {self.n}) = {self.m} | {self.n} == {self.compute()}"
        # return f"g({self.m}, {self.n}) = {self.m} & {self.n} == {self.compute()}"

    def compute(self) -> int:
        # return (self.m ^ self.n) + (self.m | self.n) + (self.m & self.n)
        # return self.m ^ self.n
        # return self.m | self.n
        # return self.m & self.n
        return (self.m | self.n)


"""
XOR diagonals:
g(0, n) = +1, repeat
g(1, n-1) = -1, then +3, repeat
g(2, n-2) =
2, 3, 0, 1, 6, 7, 4, 5, 4, 10


"""

# def compute(m: int, n: int) -> int:
#     return m ^ n + m | n + m & n


def compute(N: int) -> int:
    debug_sums = {}
    my_sums = {}
    half_power_of_two = 1
    power_of_two = 1
    for _ in range(int(math.log(N, 2)) + 1):
        power_of_two *= 2
        for number in range(half_power_of_two, N + 1):
            remainder = number % power_of_two
            factor_left = abs(half_power_of_two - remainder - 1) + half_power_of_two
            factor_right = number // power_of_two
            summand_after = 0
            if remainder >= half_power_of_two:
                summand_after = 2 * (remainder - half_power_of_two + 1)
            value = factor_left * factor_right + summand_after
            debug_sums[half_power_of_two] = debug_sums.get(half_power_of_two, [])
            debug_sums[half_power_of_two].append(value)
            my_sums[half_power_of_two] = my_sums.get(half_power_of_two, 0) + value
        half_power_of_two = power_of_two
    corrected = {factor: factor * value for factor, value in my_sums.items()}
    result = 2 * sum(corrected.values())

    return result


def main():
    my_sum = []
    target = 17

    for n in range(target + 1):
        partial_sum = []
        for k in range(n + 1):
            a = Formula(k, n - k)
            partial_sum.append(a.compute())
        my_sum.append(partial_sum)

    print(f"g(k, n-k)")
    for row in my_sum:
        print(" ".join(map(str, row)))

    max_value = max(i for row in my_sum for i in row)
    i = 0
    while 1:
        print_triangle = []
        two = 2**i
        if max_value < two:
            break
        for row in my_sum:
            print_row = []
            for cell in row:
                print_row.append(int(cell | two == cell))
            print_triangle.append(print_row)
        print(f"\nnumber | {two} == number")
        for row in print_triangle:
            row_copy = row.copy()
            row_copy.insert(0, sum(row))
            print(sum(row))
            # print(" ".join(map(str, row_copy)))
            # print(" ".join(map(str, row)))
        i += 1

    result_10 = compute(10)
    print(f"G(10) == {result_10}")
    result_100 = compute(100)
    print(f"G(100) == {result_100}")
    result_1000 = compute(1000)
    print(f"G(1000) == {result_1000}")
    assert result_10 == 754, f"{result_10} != 754"
    assert result_100 == 583_766, f"{result_100} != 583_766"
    assert result_1000 == 580_621_308, f"{result_1000} != 580_621_308"
    # result_n = compute(10**7)

    # result = []
    # for i in my_sum:
    #     print(i)
    #     result.append(sum(i))
    # print(f"Sum for N={target}: {sum(result)}")
    # print(" ".join(map(str, [i for i in result])))
    # print(" ".join(map(str, [sum(result[:i + 1]) for i in range(len(result))])))


if __name__ == '__main__':
    main()
"""
g(k, n-k)
0
1 1
2 1 2
3 3 3 3
4 3 2 3 4
5 5 3 3 5 5
6 5 6 3 6 5 6
7 7 7 7 7 7 7 7
8 7 6 7 4 7 6 7 8
9 9 7 7 5 5 7 7 9 9
10 9 10 7 6 5 6 7 10 9 10
11 11 11 11 7 7 7 7 11 11 11 11
12 11 10 11 12 7 6 7 12 11 10 11 12
13 13 11 11 13 13 7 7 13 13 11 11 13 13
14 13 14 11 14 13 14 7 14 13 14 11 14 13 14
15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15
16 15 14 15 12 15 14 15 8 15 14 15 12 15 14 15 16
17 17 15 15 13 13 15 15 9 9 15 15 13 13 15 15 17 17

number | 1 == number
row % 2 == 0: 0 1 2 3 +1
row % 2 == 1: 2 4 6 8 +2

1-bit:
my_sum = 0
for i in range(10):
    if i % 2 == 0:
        my_sum += i // 2
    elif i % 2 == 1:
        my_sum += i + 1
        
3 * (1+2+3+...+n//2)
        
0
2
1
4
2
6
3
8
4
10
5
12
6
14
7
16
8
18

number | 2 == number
row % 4 == 0: 0 3 6 9 +3
row % 4 == 1: 0 2 4 6 +2
row % 4 == 2: 2 5 8 11 +3
row % 4 == 3: 4 8 12 16 +4

2-bit:
my_sum = 0
for i in range(10):
    if i % 4 == 0:
        if i >= 2:
            my_sum += 3*i // 4
    elif i % 4 == 1:
        if i >= 2:
            my_sum += 2*i // 4
    elif i % 4 == 2:
        if i >= 2:
            my_sum += 3*i // 4 + 2
    elif i % 4 == 3:
        if i >= 2:
            my_sum += 4*i // 4 + 4
my_sum *= 2 (because of 2-bit)

3 = 1 + 2
2 = 0 + 2
3 = 1 + 2
4 = 2 + 2

0
0
2
4
3
2
5
8
6
4
8
12
9
6
11
16
12
8

number | 4 == number
row % 8 == 0: 0 7 14 +7
row % 8 == 1: 0 6 12 +6
row % 8 == 2: 0 5 10 +5
row % 8 == 3: 0 4 8 +4
row % 8 == 4: 2 7 12 +5
row % 8 == 5: 4 10 16 +6
row % 8 == 6: 6 13 20 +7
row % 8 == 7: 8 16 24 +8

0
0
0
0
2
4
6
8
7
6
5
4
7
10
13
16
14
12

number | 8 == number
row % 16 == 0: +15, starts at 0
row % 16 == 1: +14, starts at 0
row % 16 == 2: +13, starts at 0
row % 16 == 3: +12, starts at 0
...
row % 16 == 7: +8, starts at 0
row % 16 == 8: +9, starts at 2
row % 16 == 9: +10, starts at 4
...
row % 16 == 15: +16, starts at 16

0
0
0
0
0
0
0
0
2
4
6
8
10
12
14
16
15
14

number | 16 == number
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
2
4
"""
