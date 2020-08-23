class Solution:
    def toGoatLatin(self, S: str) -> str:
        return " ".join(
            (word if word[0].lower() in "aeiou" else word[1:] + word[0]) + f"m{'a'*i}"
            for i, word in enumerate(S.split(" "), start=2)
        )


# fmt: off
test_cases = [
    "I speak Goat Latin",
    "The quick brown fox jumped over the lazy dog",
]
results = [
    "Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
    "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case
        my_result = app.toGoatLatin(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
