from typing import List, Dict
from collections import deque

# TOO SLOW
class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = words
        self.keep_track = deque()
        self.word_counter: Dict[str, List[str]] = {word: list(word) for word in words}
        self.longest_word = max(len(i) for i in words)
        self.words_ending_with_char = {}
        for i in words:
            char = i[-1]
            if char not in self.words_ending_with_char:
                self.words_ending_with_char[char] = [i]
            else:
                self.words_ending_with_char[char].append(i)

    def query(self, letter: str) -> bool:
        self.keep_track.append(letter)
        if len(self.keep_track) > self.longest_word:
            self.keep_track.popleft()
        for word in self.words_ending_with_char.get(letter, []):
            if word[-1] == letter:
                word_as_list = self.word_counter[word]
                if len(self.keep_track) >= len(word) and all(
                    i == j for i, j in zip(word_as_list[::-1], reversed(self.keep_track))
                ):
                    return True
        return False


if __name__ == "__main__":
    # fmt: off
    s = StreamChecker(["ab", "ba", "aaab", "abab", "baa"])
    q = ["a","a","a","a","a","b","a","b","a","b","b","b","a","b","a","b","b","b","b","a","b","a","b","a","a","a","b","a","a","a"]
    expected = [False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False]
    # fmt: on

    for query, expect in zip(q, expected):
        value = s.query(query)
        print(query, value, expect)
        assert value is expect
