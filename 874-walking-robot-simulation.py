# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)
                    else:
                        break

        return ans
        

if __name__ == "__main__":
    s = Solution()
    print(s.robotSim([4,-1,3], []))