class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string_split = str.split(" ")
        if len(pattern) != len(string_split):
            return False

        set_of_pattern = set(pattern)
        set_of_string = set(string_split)
        if len(set_of_pattern) != len(set_of_string):
            return False

        assigned_chars = {}
        already_assigned_words = set()
        for char, word in zip(pattern, str.split(" ")):
            if word not in already_assigned_words:
                assigned_chars[char] = word
                already_assigned_words.add(word)
            elif assigned_chars.get(char, "") != word:
                return False
        return True


if __name__ == "__main__":
    # fmt: off
    test_cases = [
        ["abba", "dog cat cat dog"],
        ["abba", "dog cat cat fish"],
        ["aaaa", "dog cat cat dog"],
        ["abba", "dog dog dog dog"],
    ]
    results = [
        True,
        False,
        False,
        False,
    ]
    # fmt: on

    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.copy() if hasattr(test_case, "copy") else test_case
        my_result = app.wordPattern(*test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
