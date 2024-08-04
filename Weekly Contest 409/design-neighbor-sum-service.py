# https://leetcode.com/contest/weekly-contest-409/problems/design-neighbor-sum-service/description/
class neighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        index = self.find_value_index(value)
        if not index:
            return None

        index_delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        return sum(self.try_get_value(index[0] + i, index[1] + j) for i, j in index_delta)

    def diagonalSum(self, value: int) -> int:
        index = self.find_value_index(value)
        if not index:
            return None

        index_delta = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        return sum(self.try_get_value(index[0] + i, index[1] + j) for i, j in index_delta)

    def try_get_value(self, i: int, j: int) -> int:
        if 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0]):
            return self.grid[i][j]
        return 0

    def find_value_index(self, value: int) -> tuple[int]:
        for i in range(len(self.grid)):
            if value in self.grid[i]:
                return i, self.grid[i].index(value)
        return None

if __name__ == "__main__":
    grid = [[[0,1,2],[3,4,5],[6,7,8]]]