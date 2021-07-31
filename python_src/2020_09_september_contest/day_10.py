from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # print(secret, guess)
        correct_exactly = 0
        counter_secret = Counter()
        counter_guess = Counter()
        for i1, i2 in zip(secret, guess):
            if i1 == i2:
                correct_exactly += 1
                continue
            counter_secret[i1] += 1
            counter_guess[i2] += 1

        correct_numbers = 0
        for digit, amount in counter_guess.items():
            target_amount = counter_secret[digit]
            correct_numbers += min(target_amount, amount)
            # print(digit, amount, target_amount)
        return f"{correct_exactly}A{correct_numbers}B"


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        ["1807", "7810"],
        ["1123", "0111"],
    ]
    results = [
        "1A3B",
        "1A1B",
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.getHint(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
