from typing import List, Tuple


class Solution:
    def __init__(self):
        self.newly_rotten = []
        self.minute = 0
        self.grid = []

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.newly_rotten = []
        self.fresh_oranges = []
        self.minute = 0
        self.grid = grid

        # Grab initially rotten oranges
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 2:
                    self.newly_rotten.append((y, x))
                elif value == 1:
                    self.fresh_oranges.append((y, x))

        if not self.newly_rotten and self.fresh_oranges:
            return -1
        if not self.fresh_oranges:
            return 0

        while self.newly_rotten:
            rotten_this_minute = []
            for rotten_cell in self.newly_rotten:
                rotten_this_minute += self.rot_neighbors(rotten_cell)

            if not rotten_this_minute:
                if not self.get_fresh_oranges():
                    return self.minute
                else:
                    return -1
            self.minute += 1
            self.newly_rotten = rotten_this_minute

    def get_fresh_oranges(self):
        fresh_oranges = []
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 1:
                    fresh_oranges.append((y, x))
        return fresh_oranges

    def rot_neighbors(self, cell: Tuple[int, int]) -> List[Tuple[int, int]]:
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        newly_rotten = []
        for offset in offsets:
            new_cell = self.add_cell(cell, offset)
            if new_cell[0] < 0 or new_cell[1] < 0 or new_cell[0] >= len(self.grid) or new_cell[1] >= len(self.grid[0]):
                continue
            y, x = new_cell
            new_cell_value = self.grid[y][x]
            if new_cell_value == 1:
                self.grid[y][x] = 2
                newly_rotten.append(new_cell)
        return newly_rotten

    def add_cell(self, cell: Tuple[int, int], other: Tuple[int, int]):
        return (cell[0] + other[0], cell[1] + other[1])


""" Best solution
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        toVisit = []
        nextMinuteVisit = []
        freshOranges = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    toVisit.append((i,j))
                elif(grid[i][j] == 1):
                    freshOranges += 1
                    
        # BFS from every rotten orange
        # If at the end there exists a fresh orange we return.
        while len(toVisit) > 0:
            currentPoint = toVisit.pop(0)

            x = currentPoint[0]
            y = currentPoint[1]
            
            if x+1 < len(grid) and grid[x+1][y] == 1: 
                nextMinuteVisit.append((x+1, y))
                grid[x+1][y] = 2
                freshOranges -= 1
            if x-1 >= 0 and grid[x-1][y] == 1: 
                nextMinuteVisit.append((x-1, y))
                grid[x-1][y] = 2
                freshOranges -= 1
            if y+1 < len(grid[0]) and grid[x][y+1] == 1: 
                nextMinuteVisit.append((x, y+1))
                grid[x][y+1] = 2
                freshOranges -= 1
            if y-1 >= 0 and grid[x][y-1] == 1: 
                nextMinuteVisit.append((x, y-1))
                grid[x][y-1] = 2
                freshOranges -= 1
                
            if len(toVisit) == 0 and len(nextMinuteVisit) > 0:
                toVisit = nextMinuteVisit
                nextMinuteVisit = []
                minutes += 1
        
        # Check if any oranges are still fresh
        if freshOranges > 0:
            return -1
        
        return minutes
"""


# fmt: off
test_cases = [
    [[2,1,1],[1,1,0],[0,1,1]],
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0,2]],
    [[0]]
]
results = [
    4,
    -1,
    0,
    0
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        my_result = app.orangesRotting(test_case)
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case}"
