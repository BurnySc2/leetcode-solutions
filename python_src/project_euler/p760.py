from dataclasses import dataclass
import math


@dataclass
class Formula:
    m: int
    n: int

    def __str__(self):
        return f"g({self.m}, {self.n}) = {self.m} ^ {self.n} + {self.m} | {self.n} + {self.m} & {self.n} == {self.compute()}"
        # return f"g({self.m}, {self.n}) = {self.m} ^ {self.n} == {self.compute_slow()}"
        # return f"g({self.m}, {self.n}) = {self.m} | {self.n} == {self.compute_slow()}"
        # return f"g({self.m}, {self.n}) = {self.m} & {self.n} == {self.compute_slow()}"

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

# def compute_slow(m: int, n: int) -> int:
#     return m ^ n + m | n + m & n


def sum_formula(n: int) -> int:
    return n * (n + 1) // 2


"""
"""


def sum_formula_general(a: int, d: float, n: int) -> int:
    """
    SUM k=0 to n-1 of (a + k*d)
    = n/2 (2a + (n-1)d)
    https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
    a = first term
    d = difference between terms
    n = amount of terms
    """
    assert n > 0, n
    return n * (2 * a + int((n - 1) * d)) // 2


def sum_formula_general_from_zero(d: int, n: int) -> int:
    """
    SUM k=0 to n-1 of (k*d)
    = n/2 ((n-1)d)
    https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
    d = difference between terms
    n = amount of terms
    """
    assert n > 0, n
    return n * (n - 1) * d // 2


def calc_avg(start: float, end: float) -> float:
    return (start + end) / 2


def compute_faster(N: int) -> int:
    debug_sums = {}
    my_sums = {}
    half_power_of_two = 1
    power_of_two = 1

    for _ in range(int(math.log(N, 2)) + 1):
        power_of_two *= 2
        start_value = 2
        terms_amount, max_remainder = divmod(N, power_of_two)
        """
        TODO instead of looping over remainder:
        define min and max remainder, then put it into 3 categories
        cat1 < cat2 < half_power_of_two <= cat3
        cat1 < half_power_of_two <= cat2 < cat3
        or sometimes it suffices:
        cat1 < half_power_of_two <= cat2
        
        then calculate the averages on those instead
        
        cat1 = 0 
        cat2 = max_remainder 
        cat3 = power_of_two - 1
        """

        result = 0
        result12 = 0
        result34 = 0
        top_correction = 0
        bottom_correction = 0
        if half_power_of_two > 0 and terms_amount >= 0:
            # TOP CALCULATION - remainder 0 to half_power_of_two
            top1_increment = power_of_two - 1
            top1 = calc_avg(top1_increment, top1_increment * (terms_amount - 1))
            top2_increment = half_power_of_two
            top2 = calc_avg(top2_increment, top2_increment * (terms_amount - 1))

            top12 = calc_avg(top1, top2)
            amount_12_terms = half_power_of_two
            result12 = top12 * amount_12_terms * (terms_amount - 1)

            if 0 <= max_remainder < power_of_two:
                top_correction_start = top1_increment * terms_amount
                increment = -terms_amount
                top12_correction_terms = half_power_of_two
                if 0 <= max_remainder < half_power_of_two:
                    top12_correction_terms = max_remainder + 1
                top_correction = sum_formula_general(top_correction_start, increment, top12_correction_terms)


            # BOTTOM CALCULATION - remainder half_power_of_two to power_of_two
            bottom1_increment = half_power_of_two + 1
            bottom1 = calc_avg(2, 2 + bottom1_increment * (terms_amount - 1))
            bottom2_increment = power_of_two
            bottom2 = calc_avg(bottom2_increment, bottom2_increment * terms_amount)

            bottom12 = calc_avg(bottom1, bottom2)
            result34 = bottom12 * amount_12_terms * terms_amount

            if half_power_of_two == 32:
                print()

            if half_power_of_two <= max_remainder < power_of_two:
                bottom_correction_start = 2 + bottom1_increment * terms_amount
                increment = 2+terms_amount
                bottom12_correction_terms = (max_remainder % half_power_of_two) + 1
                bottom_correction = sum_formula_general(bottom_correction_start, increment, bottom12_correction_terms)

            result = result12 + result34 + top_correction + bottom_correction

        for remainder in range(power_of_two):
            this_remainder_terms_amount = terms_amount + int(max_remainder >= remainder)
            if this_remainder_terms_amount == 0 or this_remainder_terms_amount == 1 and remainder < half_power_of_two:
                continue
            debug_sums[half_power_of_two] = debug_sums.get(half_power_of_two, {})
            debug_sums[half_power_of_two][remainder] = debug_sums[half_power_of_two].get(remainder, [])
            if remainder >= half_power_of_two:
                if this_remainder_terms_amount == 1:
                    value = start_value
                    debug_sums[half_power_of_two][remainder].append(f"{value} * 1")
                    debug_sums[half_power_of_two][remainder].append(f"some filler")
                else:
                    difference_between_terms = abs(half_power_of_two - remainder - 1) + half_power_of_two
                    debug_sums[half_power_of_two][remainder].append(
                        f"E {start_value} {difference_between_terms} {this_remainder_terms_amount}"
                    )
                    end_value = start_value + ((this_remainder_terms_amount - 1) * difference_between_terms)
                    avg = (start_value + end_value) / 2
                    value = int(avg * this_remainder_terms_amount)
                    debug_sums[half_power_of_two][remainder].append(f"{avg} * {this_remainder_terms_amount}")
            else:
                difference_between_terms = abs(half_power_of_two - remainder - 1) + half_power_of_two
                debug_sums[half_power_of_two][remainder].append(
                    f"E 0 {difference_between_terms} {this_remainder_terms_amount}"
                )
                if this_remainder_terms_amount == 2:
                    value = difference_between_terms
                    debug_sums[half_power_of_two][remainder].append(f"{value / 2} * 2")
                else:
                    end_value = (this_remainder_terms_amount - 1) * difference_between_terms
                    avg = (difference_between_terms + end_value) / 2
                    value = int(avg * (this_remainder_terms_amount - 1))
                    debug_sums[half_power_of_two][remainder].append(f"{avg} * {this_remainder_terms_amount - 1}")

            debug_sums[half_power_of_two][remainder].append(value)
            my_sums[half_power_of_two] = my_sums.get(half_power_of_two, 0) + value
            if remainder >= half_power_of_two:
                start_value += 2
        debug_sums[half_power_of_two]["topsum"] = sum(
            debug_sums[half_power_of_two].get(r, [0, 0, 0])[2] for r in range(half_power_of_two)
        )
        debug_sums[half_power_of_two]["bottomsum"] = sum(
            debug_sums[half_power_of_two].get(r, [0, 0, 0])[2] for r in range(half_power_of_two, power_of_two)
        )
        debug_sums[half_power_of_two]["slowsum"] = sum(
            debug_sums[half_power_of_two].get(r, [0, 0, 0])[2] for r in range(power_of_two)
        )
        debug_sums[half_power_of_two]["quicktop"] = result12 + top_correction
        debug_sums[half_power_of_two]["quickbottom"] = result34 + bottom_correction
        debug_sums[half_power_of_two]["quicksum"] = result

        half_power_of_two = power_of_two
    corrected = {factor: factor * value for factor, value in my_sums.items() if isinstance(factor, int)}
    result = 2 * sum(corrected.values())
    return result


# def compute_faster(N: int) -> int:
#     debug_sums = {}
#     my_sums = {}
#     half_power_of_two = 1
#     power_of_two = 1
#
#     for _ in range(int(math.log(N, 2)) + 1):
#         power_of_two *= 2
#         start_value = 2
#         terms_amount, max_remainder = divmod(N, power_of_two)
#         for remainder in range(power_of_two):
#             difference_between_terms = abs(half_power_of_two - remainder - 1) + half_power_of_two
#             this_remainder_terms_amount = terms_amount + int(max_remainder >= remainder)
#             if this_remainder_terms_amount == 0 or this_remainder_terms_amount == 1 and remainder < half_power_of_two:
#                 continue
#             debug_sums[half_power_of_two] = debug_sums.get(half_power_of_two, {})
#             debug_sums[half_power_of_two][remainder] = debug_sums[half_power_of_two].get(remainder, [])
#             if remainder >= half_power_of_two:
#                 value = sum_formula_general(start_value, difference_between_terms, this_remainder_terms_amount)
#                 debug_sums[half_power_of_two][remainder].append(f"E {start_value} {difference_between_terms} {this_remainder_terms_amount}")
#             else:
#                 value = sum_formula_general_from_zero(difference_between_terms, this_remainder_terms_amount)
#                 debug_sums[half_power_of_two][remainder].append(f"E 0 {difference_between_terms} {this_remainder_terms_amount}")
#             debug_sums[half_power_of_two][remainder].append(value)
#             my_sums[half_power_of_two] = my_sums.get(half_power_of_two, 0) + value
#             if remainder >= half_power_of_two:
#                 start_value += 2
#         half_power_of_two = power_of_two
#     corrected = {factor: factor * value for factor, value in my_sums.items() if isinstance(factor, int)}
#     result = 2 * sum(corrected.values())
#     return result


def compute_slow(N: int) -> int:
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
            debug_sums[half_power_of_two] = debug_sums.get(half_power_of_two, {})
            debug_sums[half_power_of_two][remainder] = debug_sums[half_power_of_two].get(remainder, [])
            debug_sums[half_power_of_two][remainder].append(value)
            my_sums[half_power_of_two] = my_sums.get(half_power_of_two, 0) + value
        half_power_of_two = power_of_two
    corrected = {factor: factor * value for factor, value in my_sums.items() if isinstance(factor, int)}
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

    # max_value = max(i for row in my_sum for i in row)
    # i = 0
    # while 1:
    #     print_triangle = []
    #     two = 2**i
    #     if max_value < two:
    #         break
    #     for row in my_sum:
    #         print_row = []
    #         for cell in row:
    #             print_row.append(int(cell | two == cell))
    #         print_triangle.append(print_row)
    #     print(f"\nnumber | {two} == number")
    #     for row in print_triangle:
    #         row_copy = row.copy()
    #         row_copy.insert(0, sum(row))
    #         print(sum(row))
    #         # print(" ".join(map(str, row_copy)))
    #         # print(" ".join(map(str, row)))
    #     i += 1

    result_10 = compute_slow(10)
    # result2_10 = compute_faster(10)
    print(f"G(10) == {result_10}")
    # print(f"G(10) == {result2_10}")

    result_100 = compute_slow(100)
    result2_100 = compute_faster(100)

    # import time
    #
    # t1 = time.perf_counter()
    # _ = compute_faster(10**6)
    # t2 = time.perf_counter()
    # print(f"{t2 - t1}")

    print(f"G(100) == {result_100}")
    print(f"G(100) == {result2_100}")

    result_1000 = compute_slow(1000)
    result2_1000 = compute_faster(1000)
    print(f"G(1000) == {result_1000}")
    print(f"G(1000) == {result2_1000}")

    assert result_10 == 754, f"{result_10} != 754"
    assert result_100 == 583_766, f"{result_100} != 583_766"
    assert result_1000 == 580_621_308, f"{result_1000} != 580_621_308"
    # result_n = compute_slow(10**7)

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
