# https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
        Logic is using the directions to move the grid, and add the grid to the result list and check the boundary and visited set
        keep the step + 1 at 2 times change direction since it's spiral matrix
        """

        # TODO: if a point is outside the boundary, there are much step can be omitted to reduce the time complexity
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1), # left
            (-1, 0)  # up
        ]

        result = []
        visted = set()

        r = rStart  
        c = cStart
        step = 1  # refer to the current grid length, will add 1 at 2 times change direction
        direction_index = 0
        change_direction = False


        while len(result) < rows * cols:
            # print(f"r: {r}, c: {c}, step: {step}, direction_index: {direction_index}, change_direction: {change_direction}")
            for _ in range(step):
                # print(f"Current grid: {r}, {c}, In visited: {visted}")
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visted:
                    result.append([r, c])
                    visted.add((r, c))
                    # print(f"(r, c) added to result: {result}")
                
                r += directions[direction_index][0]
                c += directions[direction_index][1]

            direction_index = (direction_index + 1) % 4

            if change_direction:
                step += 1
                change_direction = False
            else:
                change_direction = True
            continue

        return result
    

if __name__ == "__main__":
    s = Solution()

    rows, cols, rStart, cStart = 1, 4, 0, 0
    print(s.spiralMatrixIII(rows, cols, rStart, cStart))

    rows, cols, rStart, cStart = 5, 6, 1, 4
    print(s.spiralMatrixIII(rows, cols, rStart, cStart))