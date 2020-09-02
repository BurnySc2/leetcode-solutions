from typing import List, Set


def sieve_of_eratosthenes(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = [True for _ in range(0, limit)]
    sieve[:2] = [False, False]
    sieve[4::2] = [False] * len(sieve[4::2])

    value = 3
    primes = [2]
    while value < limit:
        if sieve[value]:
            primes.append(value)
            sieve[value ** 2 :: value] = [False] * len(sieve[value ** 2 :: value])
        value += 2
    return primes


def prime_factors(n: int, primes: List[int] = None) -> Set[int]:
    if primes is None:
        primes = sieve_of_eratosthenes(int(n ** 0.5 + 1))
    i = 0
    factors = set()
    while n > 1 and i < len(primes):
        prime = primes[i]
        assert prime <= n
        while n % prime == 0:
            factors.add(prime)
            n //= prime
        i += 1
    if n > 1:
        factors.add(n)
    return factors


class Network:
    def __init__(self, divisors: Set[int], amount=1):
        self.divisors: Set[int] = divisors
        self.amount: int = amount

    def overlap_divisors(self, divisors: Set[int]) -> bool:
        if self.divisors & divisors:
            return True
        return False

    def add_number(self, divisors: Set[int]):
        self.divisors |= divisors
        self.amount += 1

    def overlap(self, other: "Network") -> bool:
        if self.divisors & other.divisors:
            return True
        return False

    def merge(self, other: "Network"):  # -> "Network":
        self.amount += other.amount
        self.divisors |= other.divisors
        # return Network(self.divisors | other.divisors, self.amount + other.amount)


class Solution:
    def __init__(self):
        self.networks: List[Network] = []

    def largestComponentSize(self, A: List[int]) -> int:
        self.networks.clear()
        primes = sieve_of_eratosthenes(int(max(A) ** 0.5) + 1)
        for i in A:
            divisors = prime_factors(i, primes)
            for network in self.networks:
                if network.overlap_divisors(divisors):
                    network.add_number(divisors)
                    break
            else:
                # If no connection could be found, add new connection
                self.networks.append(Network(divisors))

        del divisors, network

        # Merge networks if they overlap
        i, j = 0, 1
        while 1:
            if j >= len(self.networks):
                i += 1
                j = i + 1
                if j >= len(self.networks):
                    break
            if i >= len(self.networks):
                break

            network1 = self.networks[i]
            network2 = self.networks[j]
            if network1.overlap(network2):
                network1.merge(network2)
                self.networks.pop(j)
                i = 0
                j = 1
            else:
                j += 1

        return max(i.amount for i in self.networks)


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        [4,6,15,35],
        [20,50,9,63],
        [2,3,6,7,4,12,21,39],
    ]
    results = [
        4,
        2,
        8,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.largestComponentSize(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
