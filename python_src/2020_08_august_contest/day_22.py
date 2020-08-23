from typing import List
import random


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        def weight(rect):
            x0, y0, x1, y1 = rect
            return abs((y1 - y0 + 1) * (x1 - x0 + 1))

        self.weights: List[int] = [weight(r) for r in rects]

    def pick(self) -> List[int]:
        chosen_rect = random.choices(self.rects, self.weights)[0]
        rand_x = random.randint(chosen_rect[0], chosen_rect[2])
        rand_y = random.randint(chosen_rect[1], chosen_rect[3])
        return [rand_x, rand_y]


if __name__ == "__main__":
    s = Solution([[0, 2, 1, 3]])
    r = s.pick()
    assert 0 <= r[0] <= 1
    assert 2 <= r[1] <= 3
    print(r)

    l = [s.pick() for i in range(1000)]
    x_avg = sum(i[0] for i in l) / len(l)
    y_avg = sum(i[1] for i in l) / len(l)

    print(x_avg, y_avg)
